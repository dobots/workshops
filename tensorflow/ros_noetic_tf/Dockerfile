FROM osrf/ros:noetic-desktop-full
# <package>: <version tag> 

# nvidia-container-runtime
#ENV NVIDIA_VISIBLE_DEVICES \
#    ${NVIDIA_VISIBLE_DEVICES:-all}
#ENV NVIDIA_DRIVER_CAPABILITIES \
#    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# Ensure bin/sh (default shell) is set to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# apt update
RUN apt-get update -y && apt-get install -y less nano vim

# install pip3
RUN apt-get install -y python3-pip
#RUN pip3 install --upgrade pip3
RUN pip3 install tensorflow tensorboard gym getch matplotlib progressbar IPython tqdm pyvirtualdisplay

RUN apt-get install -y ffmpeg xvfb

# ROS
# ros needs to be updated to the latest version
RUN apt-get upgrade -y
# sourcing
RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
# Fix entrypoint.sh file
RUN sed -i 's/set -e//' /ros_entrypoint.sh
# Ensures image runs bash
CMD ["bash"]
                        
