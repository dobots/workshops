FROM osrf/ros:rolling-desktop

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
# sourcing
RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
# Fix entrypoint.sh file
RUN sed -i 's/set -e//' /ros_entrypoint.sh
# Additional installs
RUN apt-get install -y ros-rolling-gazebo-ros ros-rolling-xacro ros-rolling-joint-state-publisher

# Ensures image runs bash
CMD ["bash"]
