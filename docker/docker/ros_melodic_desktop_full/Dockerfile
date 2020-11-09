FROM osrf/ros:melodic-desktop-full
# 'desktop-full' includes gazebo9

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# ROS sourcing
RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
# Fix entrypoint.sh file
RUN sed -i 's/set -e//' /ros_entrypoint.sh

# Ensures bin/sh (default shell) is set to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update -y && apt-get install -y less nano
# Additional ROS packages

# Ensures image runs bash
CMD ["bash"]