FROM ros:melodic-ros-core-bionic

RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc

RUN apt-get update -y
RUN apt-get install -y less nano
RUN apt-get install -y ros-melodic-turtlesim ros-melodic-rqt-robot-steering ros-melodic-rqt-robot-monitor ros-melodic-rqt-common-plugins ros-melodic-rqt
