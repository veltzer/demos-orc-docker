# shellcheck shell=bash
GID=$(id -g)
export RUN_ARGS="-it --user ${UID}:${GID} --volume ${PWD}/data:/data"
