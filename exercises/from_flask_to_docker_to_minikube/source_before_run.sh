# shellcheck shell=bash
rm -rf data || true
mkdir data
export RUN_ARGS="--user \"${UID}:${UID}\" --detach --volume \"${PWD}/data:/data\" --network host"
