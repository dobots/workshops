This repository explains how to use MakeHuman and Blender to model and animate human models for use in Gazebo.

Prequisite:
- workshop/docker
- ROS Summerchool Day 2

Lines which include '$' as a precursor are terminal commands.

This workshop heavily follows the tutorial, this tutorial is slightly outdated thus will not be used for the first part of this workshop:
https://prabhjotkaurgosal.com/create-animated-human-models-for-gazebo-using-makehuman-and-blender/

Start a Docker container in 'workshops/makehuman'

Change to directory of the workshop 'mh_ws'
$ cd /projects/mh_ws

STEP 1 (Adding repositories)
Add necesarry repositories:

$ sudo add-apt-repository ppa:thomas-schiex/blender

$ sudo add-apt-repository ppa:makehuman-official/makehuman-community

STEP 2 (Installing necesarry programs)
Install Blender:

$ sudo apt-get install blender

To install MakeHuman (Do not install 'makehuman' without '-community':

$ sudo apt-get install makehuman-community



STEP3 (Configure Plugins)

Configuring MHX2.
The following terminal commands will automatically configure the plugins. You may also follow the instructions given at the repository.
https://github.com/makehumancommunity/mhx2-makehuman-exchange
It is recommended to have the MHX2 README.md  open.


$ cd /projects/mh_ws/

$ cp -R src/mhx2-makehuman-exchange/9_export_mhx2/ /usr/share/makehuman-community/plugins/

Configure MHX2 in Blender


Configure
