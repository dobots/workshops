FROM ros:rolling-ros-core-focal
# FROM osrf/ros:rolling-desktop
# <package>: <version_tag>


RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
RUN sed -i 's/set -e//' /ros_entrypoint.sh

RUN apt-get update -y
RUN apt-get install -y less nano
RUN apt-get install -y ros-rolling-turtlesim ros-rolling-rqt-robot-steering ros-rolling-rqt-robot-monitor ros-rolling-rqt-common-plugins ros-rolling-rqt 
RUN apt-get install -y python3-argcomplete
RUN apt-get install -y git 
RUN apt-get install -y python3-rosdep
RUN rosdep init -y
RUN rosdep update -y
RUN apt-get install -y python3-colcon-common-extensions
RUN apt-get install -y make
RUN apt-get install -y g++
