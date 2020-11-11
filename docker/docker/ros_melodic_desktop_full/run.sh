#!/bin/bash

#check if there is a /build and /devel in the current PWD
if [ -f devel/.catkin ]; then
echo "Starting from Catkin Workspace: $PWD, preparing it's ROS_PACKAGE_PATH."

# If you start this script inside a catkin workspace, it will make that workspace available in the projects src folder
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
    --name="ros_melodic_desktop_full" \
    ros_melodic_desktop_full \
    bash

# Note:
# Pop OS nvidia drivers give some issues.
# Go for this fix:
# https://github.com/NVIDIA/nvidia-docker/issues/1114
# Also remember to downgrade: libnvidia-container-tools:amd64 (1.3.0-1pop1~1601490873~18.04~cb62a8d, 1.3.0-1), nvidia-container-runtime:amd64 (3.4.0-1pop1~1601325114~18.04~2880fc6, 3.4.0-1), libnvidia-container1:amd64 (1.3.0-1pop1~1601490873~18.04~cb62a8d, 1.3.0-1)