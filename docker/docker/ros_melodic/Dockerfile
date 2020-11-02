FROM ros:melodic-ros-core-bionic

RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
RUN sed -i 's/set -e//' /ros_entrypoint.sh

RUN apt-get update -y
RUN apt-get install -y less nano
RUN apt-get install -y ros-melodic-turtlesim ros-melodic-rqt-robot-steering ros-melodic-rqt-robot-monitor ros-melodic-rqt-common-plugins ros-melodic-rqt

RUN apt-get install python3-argcomplete
RUN apt-get install git
RUN apt-get install python3-rosdep
RUN rosdep init
RUN rosdep update
RUN apt-get install python3-colcon-common-extensions
RUN apt-get install make
RUN apt-get install g++
