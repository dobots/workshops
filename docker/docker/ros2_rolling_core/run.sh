#!/bin/bash



#check if there is a /build and /devel in the current PWD
if [ -f devel/.catkin ]; then
echo "Starting from Catkin Workspace: $PWD, preparing it's ROS_PACKAGE_PATH."

sed -i 's/;\/projects\/src//' devel/.catkin
echo -n "`cat devel/.catkin`;/projects/src" > devel/.catkin

fi

docker run -iPt \
    --rm \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$XAUTHORITY:$XAUTHORITY" \
    --env="XAUTHORITY=$XAUTHORITY" \
    --volume="$PWD:/projects" \
    --runtime=nvidia \
    --name="ros2_rolling_core" \
    ros2_rolling_core \
    bash

# If not using Nvidia drivers, remove the '--runtime=nvidia' and add '--device=/dev/dri' (http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration)
