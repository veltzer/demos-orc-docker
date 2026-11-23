#!/bin/bash -e
if [[ -f "source_before_run.sh" ]]
then
	# shellcheck source=/dev/null
	source source_before_run.sh
else
	RUN_ARGS="-it --rm"
fi
image_name=$(basename "${PWD}")
if { docker ps --filter "name=${image_name}" --format '{{.Names}}' || true; } | grep -q "${image_name}"
then
	echo "Container [${image_name}] is running. Killing..."
	docker kill "${image_name}" || true
	sleep 5
fi

if { docker ps -a --filter "name=${image_name}" --format '{{.Names}}' || true; } | grep -q "${image_name}"
then
	echo "Container [${image_name}] is dead. Removing..."
	docker rm "${image_name}"
fi
# RUN_ARGS is a space separated option string, split it into words on purpose
read -r -a run_args <<< "${RUN_ARGS}"
docker run "${run_args[@]}" --name "${image_name}" "${image_name}"
