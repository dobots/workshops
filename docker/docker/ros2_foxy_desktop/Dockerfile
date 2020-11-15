FROM osrf/ros:foxy-desktop

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# Ensure bin/sh (default shell) is set to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# apt update
RUN apt-get update -y && apt-get install -y less nano

# ROS
# ros foxy needs to be updated to the latest version
RUN apt-get upgrade -y
# sourcing
RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
# Fix entrypoint.sh file
RUN sed -i 's/set -e//' /ros_entrypoint.sh
# Additional installs (Optional)
RUN apt-get install -y psmisc ros-foxy-xacro ros-foxy-joint-state-publisher ros-foxy-cartographer-ros ros-foxy-nav2-bringup
# Gazebo (Optional)
RUN apt-get install -y gazebo11 libgazebo11-dev ros-foxy-gazebo-ros-pkgs
RUN echo ". /usr/share/gazebo/setup.sh" >> ~/.bashrc

# Ensures image runs bash
CMD ["bash"]