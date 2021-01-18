# Webots: robot simulator


## Installation

Download the **webots_2021a_amd64.deb** file from the official website:
```
https://github.com/cyberbotics/webots/releases/tag/R2021a
```

Then move to the directory, where the file is and install it:
```
sudo apt install ./webots_2021a_amd64.deb
```

## Getting started with Webots

### 1. Starting webots
Open a terminal and type webots to launch Webots:
```
webots
```
### 2. Have a look at the demo worlds

### 3. The User Interface

 - 3D view (Tools->3D view)
	-   **Translation**: To move an object parallel to the ground: hold down the  ⇧ shift  key, press the left mouse button and drag.
	-   **Rotation**: To rotate an object around the world's vertical axis: hold down the  ⇧ shift  key, press the right mouse button and drag.
	-   **Lift**: To raise or lower an object: hold down the  ⇧ shift  key, press both left and right mouse buttons (or the middle button) and drag. Alternatively, the mouse wheel combined with the  ⇧ shift  key can also be used.
	- **Applying a Force** : To apply a force to an object, place the mouse pointer where the force will apply, hold down the  ctrl  key together with the  alt  key and left mouse button together while dragging the mouse. 
	- **Applying a Torque**: To apply a torque to an object, place the mouse pointer on it, hold down the  ctrl key together with the alt  key  and right mouse button together while dragging the mouse. 

>
 - Scene Tree (Tools->Scene Tree)
 - Text Editor (Tools-> Text Editor)
 - Console
 - Time, Play/Pause simulation

## 4.  Tutorials
We are going to follow the tutorials from the official Webots documentation:
[cyberbotics.com/doc/guide/tutorials](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots) 

## 5. Solutions
To compare your world with the solution, go to your files and find the folder named "my_first_simulation" created in  [Tutorial 1](https://cyberbotics.com/doc/guide/tutorial-1-your-first-simulation-in-webots), then go to the "worlds" folder and open with a text editor the right world.  [This solution](https://github.com/cyberbotics/webots/blob/released/projects/samples/tutorials/worlds/collision_avoidance.wbt)  as the others is located in the  [solution directory](https://github.com/cyberbotics/webots/blob/released/projects/samples/tutorials/worlds/).
Now you can compare the two files in a text editor.

To load the solution world directly into webots go to:  File-> Open Sample World -> samples-> tutorials
