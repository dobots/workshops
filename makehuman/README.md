
#  Create animated models with for Gazebo using MakeHuman and Blender
This repository explains how to use MakeHuman and Blender to model and animate human models for use in Gazebo.

# Table of Contents
1. [Prequisite](#Prequisite)
2. [Adding repositories](#Adding-repositories)
3. [Configure Plugins and Addons](#Configure-Plugins-and-Addons)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)

# Prequisite:
- workshop/docker
- ROS Summerchool Day 2

This tutorial assumes you are working in an environment where Ros programs are installed. Specifically Gazebo will be used.

**Terminal commands have a "$"  as a precursor.**

**If blender and/or makehuman is already installed, skip to [Configure Plugins and Addons](#Configure-Plugins-and-Addons).*




This workshop heavily follows the tutorial:

https://prabhjotkaurgosal.com/create-animated-human-models-for-gazebo-using-makehuman-and-blender/

This tutorial is slightly outdated thus will not be used for the first part of this workshop:


Start a Docker container in 'workshops/makehuman'

Change to directory of the workshop 'mh_ws'

```bash
$ cd /projects/mh_ws
```

# Adding repositories
Add necesarry repositories:

```bash
$ sudo add-apt-repository ppa:thomas-schiex/blender -y
$ sudo add-apt-repository ppa:makehuman-official/makehuman-community -y
```

# Installing necesarry programs
Install Blender:
```bash
$ sudo apt-get install blender -y
```

To install MakeHuman (Do not install 'makehuman' without '-community':
```bash
$ sudo apt-get install makehuman-community -y
```


# Configure Plugins and Addons

## Configuring MHX2.

The following terminal commands will automatically configure the plugins. The configuration follows the steps outlined from the MHX2 repository, for convenience the repository has already been cloned in this workspace.
You may also follow the instructions given at the repository.
https://github.com/makehumancommunity/mhx2-makehuman-exchange
It is recommended to have the MHX2 README.md  open.

The addons/plugins are added manually by copying the plugin folder into Blender/Makehuman configuration folder.

### Configure MHX2 for Makehuman.
From the MHX2 repository copy the *9_export_mhx2* folder plugins folder of Makehuman.
```bash
$ cd /projects/mh_ws/
$ cp -R src/mhx2-makehuman-exchange/9_export_mhx2/ /usr/share/makehuman-community/plugins/
```

### Configure MHX2 for Blender
From the MHX2 repository copy the *import_runtime_mhx2* folder addons folder of Blender.

Check the version of Blender and directory name.
```bash
$ blender --version
```

```bash
$ ls /usr/share/blender/
```

Go to main directory
```bash
$ cd /projects/mh_ws/
```

Replace [VERSION] with the version and/or directory name.

```bash
$ cp -R src/mhx2-makehuman-exchange/import_runtime_mhx2 /usr/share/blender/[VERSION]/scripts/addons/
```

### Example
At the time of writing the version of Blender is 2.92:
```bash
$ blender --version
Blender 2.92.0
$ ls /usr/share/blender/
2.92
$ cp -R src/mhx2-makehuman-exchange/import_runtime_mhx2 /usr/share/blender/2.92/scripts/addons/
```


### Configure Retargetter for Blender (Formerly known as Makewalk)
Configuring retargetter for Blender is done similarly to MHX2, by cloning the git repository and then adding the folders to the addon folder.
For convenience the repository has already been cloned and included in the folder. You may also clone the repository at:

https://bitbucket.org/Diffeomorphic/retarget_bvh/src/master/


# Creating A Makehuman Model
```bash
$ cp -R src/retarget_bvh/ /usr/share/blender/2.92/scripts/addons/
```
