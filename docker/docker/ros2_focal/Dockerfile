FROM ros:rolling-ros-core-focal



RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
RUN sed -i 's/set -e//' /ros_entrypoint.sh

RUN apt-get update -y
RUN apt-get install -y less nano
RUN apt-get install -y ros-rolling-turtlesim ros-rolling-rqt-robot-steering ros-rolling-rqt-robot-monitor ros-rolling-rqt-common-plugins ros-rolling-rqt
