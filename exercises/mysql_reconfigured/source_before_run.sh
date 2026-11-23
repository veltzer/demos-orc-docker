# shellcheck shell=bash
# the password comes from .auto.enter.sh
: "${env_db_password:?set by .auto.enter.sh}"
export RUN_ARGS="--detach -e MYSQL_ROOT_PASSWORD=${env_db_password} -p 3306:3306 --rm"
