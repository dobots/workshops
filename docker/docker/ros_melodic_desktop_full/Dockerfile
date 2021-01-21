FROM osrf/ros:melodic-desktop-full-bionic
# 'desktop-full' includes gazebo9

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics


RUN apt-get -y update && apt-get install -y ros-melodic-navigation ros-melodic-hector-slam ros-melodic-teb-local-planner ros-melodic-teleop-twist-keyboard ros-melodic-hector-gazebo-plugins


# Ensure bin/sh (default shell) is set to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# apt update
RUN apt-get update -y && apt-get install -y less nano

# ROS
# sourcing
RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
# Fix entrypoint.sh file
RUN sed -i 's/set -e//' /ros_entrypoint.sh
# Additional ROS packages


# Ensures image runs bash
CMD ["bash"]
