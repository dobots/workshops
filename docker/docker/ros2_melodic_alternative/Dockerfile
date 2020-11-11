FROM ros:melodic-ros-core-bionic
# <package>: <version tag> 

RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc
RUN sed -i 's/set -e//' /ros_entrypoint.sh

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update && apt-get install -y less nano 
RUN apt-get -y install libgl1-mesa-glx libgl1-mesa-dri 

CMD ["bash"]
