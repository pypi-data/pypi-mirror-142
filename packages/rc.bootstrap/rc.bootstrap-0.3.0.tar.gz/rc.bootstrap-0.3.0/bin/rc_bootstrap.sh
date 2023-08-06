#!/bin/sh

RC_BOOTSTRAP_VERSION='0.3.0'

# ------------------------------------------------------------------------------
#
# Create a virtualenv under $RC_BASE/bootstrap/envs/, and install `rc.bootstrap`
# and `rc.io` in it.
#
# This script takes the following arguments (shown are default settings):
#
#    -b: home of RC environments          [$HOME/.rc/bootstrap/envs/]
#    -i: packages to install              ['']
#    -n: name of environment to bootstrap [rc.$RC_BOOTSTRAP_VERSION]
#    -p: commands to run before start     ['']
#    -r: command to run after completion  ['']
#
#
# All arguments are expanded with the environment of the shell running this
# script (usually the login shell).  The variable `RC_BOOTSTRAP_VERSION` will be
# automatically set to the version of the `rc.bootstrap` module and cannot be
# overwritten.
#
# The arguments`-p` and `-i` can be specified multiple times.
#
# Arguments passed to `-i` can have different formats (distingushed by URL
# schemas), and will be installed in different ways:
#
#   - pip:<module_name>
#     install: `pip install <module_name>
#     example: numpy
#     example: git+https://github.com/project/repo/branch/devel
#
#   - tar:<file_name>
#     install: tar xf <file_name>
#              pip install <file_base>
#     where <file_base> is <file_name> without extensions
#     example: numpy.tar.gz
#
# The argument passed to `-r` is `exec`ed after bootstrapping completed
# successfully.  That command will inherit pid and stdio handles from the
# bootstrapper process.
#
#
# TODO:
#  - on first of each months, remove all environments which are not used for
#    longer than 30 days.  To support that, each use should update a timestamp.
#  - use a lockfile to ensure only one bootstrapper is active at any time in
#    a specific environment dir.
#

LOG=$(mktemp)

# ------------------------------------------------------------------------------
#
out(){
    printf "$*" >> $LOG
    printf "$*"
}

err(){
    out "# \n"
    printf "ERROR: $*\n$LOG\n" >> $LOG
    printf "ERROR: $*\n$LOG\n" 1>&2
    out "# \n"
    out "# ---------------------------------------------------------------\n"
    tail -n 10 $LOG
    exit 1
}

check() {
    ret="$1"; shift
    log="$*"
    if test "$ret" = "0"
    then
        out "#\n# OK\n"
    else
        err "$log failed"
    fi
}


# ------------------------------------------------------------------------------
#
progress(){

    printf "# ["
    while read X
    do
        echo "$X" >> $LOG
        echo -n "."
    done
    printf "]\n"
}


# ------------------------------------------------------------------------------
#
pre_exec() {
    cmd="$*"
    out "#\n"
    out "# ---------------------------------------------------------------\n"
    out "#\n# run pre_exec: $cmd\n#\n"
    eval "$cmd" 2>&1 | progress
    check "$?" "pre_exec $cmd"
}


# ------------------------------------------------------------------------------
#
install() {
    spec="$1"

    out "# \n"
    out "# -------------------------------------------------------------------\n"
    out "#\n# post-install $spec\n#\n"
    schema=$(echo "$spec" | cut -f 1  -d ':')
    name=$(  echo "$spec" | cut -f 2- -d ':')

    if test "$schema" = "pip"
    then
        pip install "$name" 2>&1 | progress
        res=$?
    elif test "$schema" = "tar"
    then
        dname="$name"
        dname=$(basename "$dname" .tgz)
        dname=$(basename "$dname" .tbz)
        dname=$(basename "$dname" .gz)
        dname=$(basename "$dname" .bz)
        dname=$(basename "$dname" .bz2)
        dname=$(basename "$dname" .tar)
           tar xf "$name"       2>&1 | progress \
        && pip install "$dname" 2>&1 | progress
        res=$?
    else
        err "invalid post-install schema in '$spec'"
    fi

    check "$res" "post_install $spec"
}


# ------------------------------------------------------------------------------
# set defaults
RC_BASE="$HOME/.rc"
RC_NAME="rc.$RC_BOOTSTRAP_VERSION"
RC_EXEC=""
PRE_EXEC=''

# get paratemeter settings
while getopts "b:c:i:n:p:r:" OPTION; do
    echo "=== 1 = $OPTION = $OPTARG ="
    case $OPTION in
        b)  RC_HOME="$OPTARG"          ;;
        i)  INSTALL="$INSTALL $OPTARG" ;;
        n)  RC_NAME="$OPTARG"          ;;
        p)  pre_exec "$OPTARG"         ;;
        r)  RC_EXEC="$OPTARG"          ;;
        *)  err "Unknown option: '$OPTION'='$OPTARG'" 2>&1
    esac
done

# expand env variables.
expand(){
    dest=_expanded_var
    eval "$dest=$1"
    echo "$_expanded_var"
}

RC_BASE=$(expand '$RC_BASE')
RC_NAME=$(expand '$RC_NAME')

PYTHON=$(which python3)
PYTHON_VERSION=$($PYTHON -V)

# create a envs/' dir under $RC_BASE
ENV_LOC="$RC_BASE/bootstrap/envs/$RC_NAME"

out "# -------------------------------------------------------------------\n"
out "#\n# check setup\n#\n"
out "RC_BOOTSTARP : $RC_BOOTSTRAP_VERSION\n"
out "RC_BASE      : $RC_BASE     \n"
out "RC_NAME      : $RC_NAME     \n"
out "WGET         : $WGET        \n"
out "ENV_LOC      : $ENV_LOC     \n"
out "PYTHON       : $PYTHON [$PYTHON_VERSION]\n"

mkdir -p   "$RC_BASE/bootstrap"
cd         "$RC_BASE/bootstrap"

# ------------------------------------------------------------------------------
# capture initial environment
out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# create env $RC_NAME\n#\n"
env | sort | tee "env.$RC_NAME.orig" 2>&1 | progress

out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# create env $RC_NAME\n#\n"
$PYTHON -m venv "$ENV_LOC" python=python3 2>&1 | progress
check "$?" "venv failed"

out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# activate env $env_loc\n#\n"
. "$ENV_LOC/bin/activate" 2>&1
check "$?" "activate failed"

out "# -------------------------------------------------------------------\n"
out "#\n# install rc.bootstrap\n#\n"

# FIXME: this can be removed after release
pip install 'git@github.com:radical-consulting/bootstrap.git' 2>&1 | progress
pip install rc.bootstrap 2>&1 | progress
check "$?" "pip install 'rc.bootstrap'"

out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# install rc.io\n#\n"
pip install rc.io 2>&1 | progress
check "$?" "pip install 'rc.io'"

out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# summary\n#\n"
rc.stack
check "$?" "environment check"

# basic bootstrapping is done, the environment is valid. Install additional
# modules
for spec in $INSTALL
do
    install "$spec"
done

# Finally, capture that envirnment (including the `pre_exec` commands executed
# earlier).  We use the `radical.utils` env isolation facilities for that, which
# we know we installed as dependency of `rc.io`.
out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# capture environment\n#\n"
# env | tee "env.$RC_NAME.src" 1>&2 | progress  # current env (to capture)
. radical-utils-env.sh
env_prep -r "env.$RC_NAME.orig" -t "env.$RC_NAME.sh" 2>&1 | progress
check "$?" "capture environment"

# we won't return from the command below, so clean up before executing it.
mv -i "$ENV_LOC/log" "$ENV_LOC/log.1" 2>/dev/null || true
mv -i $LOG           "$ENV_LOC/log"

out "# \n"
out "# -------------------------------------------------------------------\n"
out "#\n# execute command\n#\n"
if test -z "$RC_EXEC"
then
    out "no command specified\n"
else
    exec $RC_EXEC
    # we should never get here...
    check "1" "execute command"
fi
out "# \n"
out "# -------------------------------------------------------------------\n"


# ------------------------------------------------------------------------------

