#!/bin/bash -eu
docker run -it \
	-e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
	-e XDG_RUNTIME_DIR=/tmp \
	-v $XDG_RUNTIME_DIR/$WAYLAND_DISPLAY:/tmp/$WAYLAND_DISPLAY \
	-v $HOME/projects:/home/dev/projects \
	--device /dev/dri \
	vscode
