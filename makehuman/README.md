This repository explains how to use MakeHuman and Blender to model and animate human models for use in Gazebo.

# Prequisite:
- workshop/docker
- ROS Summerchool Day 2


If blender and/or makehuman is already installed, skip to STEP 3 to configure plugins.




This workshop heavily follows the tutorial, this tutorial is slightly outdated thus will not be used for the first part of this workshop:
https://prabhjotkaurgosal.com/create-animated-human-models-for-gazebo-using-makehuman-and-blender/

Start a Docker container in 'workshops/makehuman'

Change to directory of the workshop 'mh_ws'

'''bash
cd /projects/mh_ws
'''

# STEP 1 (Adding repositories)
Add necesarry repositories:

'''bash
sudo add-apt-repository ppa:thomas-schiex/blender -y
sudo add-apt-repository ppa:makehuman-official/makehuman-community -y
'''
 
# STEP 2 (Installing necesarry programs)
Install Blender:
'''bash
sudo apt-get install blender -y
'''

To install MakeHuman (Do not install 'makehuman' without '-community':
'''bash
sudo apt-get install makehuman-community -y
'''


# STEP3 (Configure Plugins)

Configuring MHX2.

The following terminal commands will automatically configure the plugins. The configuration follows the steps outlined from the MHX2 repository, for convenience the repository has already been cloned in this workspace. 
You may also follow the instructions given at the repository.
https://github.com/makehumancommunity/mhx2-makehuman-exchange
It is recommended to have the MHX2 README.md  open.

Configure MHX2 for Makehuman.

'''bash
cd /projects/mh_ws/
cp -R src/mhx2-makehuman-exchange/9_export_mhx2/ /usr/share/makehuman-community/plugins/
'''

Configure MHX2 for Blender 
Check the version of Blender and directory name.
'''bash
blender --version
ls /usr/share/blender/
'''

$ cd /projects/mh_ws/

Replace [VERSION] with the version and/or directory name.

'''bash 
cp -R src/mhx2-makehuman-exchange/import_runtime_mhx2 /usr/share/blender/[VERSION]/scripts/addons/
'''

At the time of writing the version of Blender is 2.92, so the command looks like:
'''bash
cp -R src/mhx2-makehuman-exchange/import_runtime_mhx2 /usr/share/blender/2.92/scripts/addons/
'''


