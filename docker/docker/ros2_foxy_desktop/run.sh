#!/bin/bash

# check if there is a /build and /install in the current PWD
if [ -f install/local_setup.bash ]; then
echo "Starting from ROS2 Workspace: $PWD, preparing it's COLCON_CURRENT_PREFIX."

# If you start this script inside a ros2 workspace, it will make that workspace available in the projects src folder
COLCON_CURRENT_PREFIX="/projects/install"
# NOTE: To use this, you cannot use symlinks when you build with colcon!
fi

docker run -iPt \
    --rm \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$XAUTHORITY:$XAUTHORITY" \
    --env="XAUTHORITY=$XAUTHORITY" \
    --volume="$PWD:/projects" \
    --env="COLCON_CURRENT_PREFIX=$COLCON_CURRENT_PREFIX" \
    --env="DISPLAY=$DISPLAY" \
    --runtime=nvidia \
    --name="ros2_foxy_desktop" \
    ros2_foxy_desktop \
    bash