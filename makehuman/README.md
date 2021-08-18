
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
For convenience the repository has already been cloned and included in the "src" directory. You may also clone the repository at:

https://bitbucket.org/Diffeomorphic/retarget_bvh/src/master/

Clone the "retarget_bvh" directory to the addon plugin. Replace [VERSION] with the current version.

```bash
$ cp -R src/retarget_bvh/ /usr/share/blender/2.92/scripts/addons/
```

## Confirming plugins and addons.
Checking if the folders were properly moved to the correct directories. If the directory exists, the command should resturn "Directory Exists", otherwise the command would not return anything.

Checking MHX2 in Makehuman
```bash
$ [ -d /usr/share/makehuman-community/plugins/9_export_mhx2 ] && echo "Directory Exists"

Directory Exists
```

# Creating A Makehuman Model
To open the programs in the workspace execute them in separate terminals
```bash
$ blender
$ makehuman-community
```
For the creation of the models follow the instructions given at:

https://prabhjotkaurgosal.com/create-animated-human-models-for-gazebo-using-makehuman-and-blender/

and

https://www.youtube.com/watch?v=dFLPjVWjmCY

In MakeHuman you may create any human models you can.
Do not add any eyes or tongue in Geometries.

In Pose/Animate select "Cmu mb" as the Rig presets. Marked in the red square.

![Makehuman](https://i.imgur.com/ffqZzgD.png)


Export the file as MHX2 (File -> Export - > MHX2), if the installation and plugin configuration was successful, the MHX2 file type should be available in.

![Makehuman](https://i.imgur.com/j3CzX6P.png)

Open Blender in workshop via terminal.


Include the preferences.
Edit -> preferences:
MakeHuman: Import:Runtime: MakeHuman Exhcange 2 (.mhx2)

and

BVH: Retargeter

![Makehuman](https://i.imgur.com/NG7RM1t.png)


In blender import a human model.  In directory Examples, select a model to import.
