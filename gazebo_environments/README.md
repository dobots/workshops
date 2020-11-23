# How to create custom environments in Gazebo

## Dependencies:
**ros-melodic-full docker image** 
* Download from: [github.com/dobots/workshops/docker/docker/ros_melodic_desktop_full](https://github.com/dobots/workshops/tree/master/docker/docker/ros_melodic_desktop_full)
*To install Docker follow the instructions: [github.com/dobots/docker/getting_started.md](https://github.com/dobots/workshops/blob/master/docker/getting_started.md)*
* Copy the image inside your docker folder and build it:
	```
	cd ~/docker
	cd ros_melodic_desktop_full
	docker build -t ros_melodic_desktop_full .
	```
or 

**ros-melodic installation with Gazebo**

Optional: Blender installation

## I. Part:  Create your own Gazebo environment

1. Create a gazebo_environments_ws/src folder

2. Copy the content simple_shapes_description folder from this folder into your workspace src folder.
Doesn't create a symbolic link, because Docker doesn't like them ;)

3. If you would like to work inside a Docker image, follow the instructions below to start it. If you have a  ROS and Gazebo installed on your machine jump to step 4.
> **_Commands to use Docker:_** 
> 1. Move into the folder of the files you would like to use inside Docker: 
		>```
		>cd ~/<path-to-your-ros-packages>
		>cd ~/gazebo_environments_ws
		>```
>2. Start Docker:
	>```
>	~/<path-to-your-docker-image/run.sh
>	~/docker/ros_melodic_desktop_full/run.sh
>	```
>3. Inside the Docker image move into the `/projects` folder to access the files from your host folder.
>
>4. Open a new terminal inside the Docker environment:
>	```
>	docker exec -it <name-of-your-docker-image> /bin/bash
> docker exec -it ros_melodic_desktop_full /bin/bash
>	```
>5. Source the environment variables in this terminal as well:
>	```
>	. ros_entrypoint.sh
>	```

4. Inside the projects folder run `catkin_make` to build your packages
5.  After `catkin_make` don't forget to source it `source devel/setup.bash`

6. You can create a world with simple shapes or shapes from the database using directly Gazebo:
	*	Start gazebo
	*	Insert models 
	*	Choose save_as
	*	
7. Walk through the files .world file and discuss  each part
8. Launch this world: `roslaunch simple_shapes_description simple_shapes_world.launch` 

![simple shapes environment](https://github.com/dobots/workshops/blob/master/gazebo_environments/images/simple_shapes.png)


9. On your host machine copy this folder inside the src directory and rename it.

10. Open CMakeLists.txt and change the project name to the name of the folder

11. Open package.xml:
 *  change the project name to the name of the folder
 *  edit the description tag
 * fill in your email
 * choose license ( by default BSD)
 * Add a tag to the end of the file to automatically add models to the gazebo_plugin_path.

12. Update the Readme file

13. Rename your world file

14. Rename and edit your launch file

15. Create a meshes folder inside your ros package ( now you should have launch, meshes, worlds folders)

16. Dowload a mesh file (https://www.thingiverse.com/ or any other platform. Look for .stl or .dae (collada) files.
>**_NOTE:_**  To be able to add materials and different colours the .stl files can be opened and converted to Collada (.dae) format in Blender. 

17. Put the .dae or .stl file inside your meshes folder
 >**_NOTE:_** for collision a simplified model can be used

 >**_NOTE:_** Open in blender if you would like to edit the file, or colour different parts to different colours. The new blender had a bug for a while, that the colours were not saved properly. The old blender 2.x can save it properly.

18. Edit your world file:
```
 <model name="baby raptor">
    <static>true</static>
    <pose>0 0 -1.0 0 0 0</pose>
    <link name="link"> 
      <visual name="visual">
    <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://simple_shapes_mesh_description/meshes/baby_raptor.stl</uri>
          </mesh>
        </geometry>
        <cast_shadows>true</cast_shadows>
      </visual>
  <collision name="collision">
   <pose>0 0 0 0 0 0</pose>
       <geometry>
          <mesh>
            <uri>model://simple_shapes_mesh_description/meshes/baby_raptor.stl</uri>
          </mesh>
        </geometry>
      </collision>
    </link>
  </model>
```

19. Run `catkin_make`, then `source devel/setup.bash`

20. Launch your world: `roslaunch simple_shapes_mesh_description simple_shapes_mesh_world.launch`

![simple shapes environment with a custom mesh file](https://github.com/dobots/workshops/blob/master/gazebo_environments/images/simple_shapes_mesh.png)


## II. Part: Import part of a 3D map into Gazebo

### Converting 3D models from OpenStreetMap to .stl format

 1.   Select the region of interest in Open Street Map and Export it
		- Go to the website  [Open Street Map](http://www.openstreetmap.org/).
   
	   - Click the  **Export**  button at the top of the screen.

	  - Fill in the latitude and longitude coordinate range (scroll through the coordinate fields by pressing a  **Tab**  key to view an area on the map).
	  -  Click the  **Export**  button the left side of the screen (the file extension will be  _.osm_).

 2. Map editing
	- Visit the site  _https://josm.openstreetmap.de/wiki/Download_  to download the  JOSM  application  _josm-tested.jar_.

	- Open an application with the command: 

	 	 `java -jar josm-tested.jar`
	 	 
	>**_NOTE:_**	If you don't hava java installed, **install java-8 !!! Do not install openjdk-11!** It has some bugs and the 3D map creation won't work! 

	- Choose the  _.osm_  extension file.

	- Changes to map attributes are made in the right part of the application.

	- Save the changes

3. 3D Map Creation

	- Access the website  _http://osm2world.org/_  to download the  [OSM2world](http://osm2world.org/)  application.

	- Open an application with the command:

	    `java -jar OSM2World.jar`

	- Check out the changes performed in the previous step.

	- Export the file to the object format (_.obj_).

4. Conversion from  _.obj_  format to  _.stl_  format.
	
	- Install open scene graph:
		`sudo apt install openscenegraph`

	- Run the command:
	
		`osgconv map_pucrs.obj map_pucrs.stl`

	>**_Documentation:_**	 _http://www.openscenegraph.org/index.php/documentation/guides/user-guides/55-osgconv_


>**_Source:_** [Converting 3D models from OpenStreetMap to .stl format copied from: https://pucrs-campus-on-gazebo.readthedocs.io/en/latest/source/campus/](https://pucrs-campus-on-gazebo.readthedocs.io/en/latest/source/campus/)


### Create a package with the new .stl file

1. On your host machine copy the simple_shapes_mesh_description folder inside the src directory and rename it.

2. Open CMakeLists.txt and change the project name to the name of the folder

3. Open package.xml:
 *  change the project name to the name of the folder
 *  edit the description tag
 * fill in your email
 * choose license ( by default BSD)
 * Add a tag to the end of the file to automatically add models to the gazebo_plugin_path.

4. Update the Readme file

5. Rename your world file

6. Rename and edit your launch file

7. Put the previously created mesh file into your meshes folder
 >**_NOTE:_** for collision a simplified model can be used
 
>**_NOTE:_** Open in blender if you would like to edit the file, or colour different parts to different colours. The new blender had a bug for a while, that the colours were not saved properly. The old blender 2.x can save it properly.

8. Edit your world file. Remove the simple shapes and  change the mesh file description to this new mesh file:
```
 <model name="wilhelminakade">
    <static>true</static>
    <pose>0 0 0.0 0 0 0</pose>
    <link name="link"> 
      <visual name="visual">
    <pose>0 0 0 0 0 0</pose>
        <geometry>
          <mesh>
            <uri>model://wilhelminakade_description/meshes/wilhelminakade.stl</uri>
          </mesh>
        </geometry>
        <cast_shadows>true</cast_shadows>
      </visual>
  <collision name="collision">
   <pose>0 0 0 0 0 0</pose>
       <geometry>
          <mesh>
            <uri>model://wilhelminakade_description/meshes/wilhelminakade.stl</uri>
          </mesh>
        </geometry>
      </collision>
    </link>
  </model>
```

9. Run `catkin_make` then `source devel/setup.bash`

10. Launch your world: `roslaunch wilhelminakade_description wilhelminakade_world.launch`

>**_NOTE:_**  use just a couple of buildings, otherwise Gazebo might crash! You might need to edit the files in blender to simplify the meshes.


![wilhelminakade](https://github.com/dobots/workshops/blob/master/gazebo_environments/images/wilhelminakade.png)



## III.Part - Spawn a rover

1. Copy the **fox_description**  and **fox_gazebo** folder into your workspace/src folder: [github.com/dobots/rofox](https://github.com/dobots/rofox)
 
  2. Walk through the included files:
  

2. Open a new terminal:
		 ```
		 docker exec -it ros_melodic_desktop_full /bin/bash
		. ros_entrypoint.sh
		cd projects
		source devel/setup.bash
		```

3. Launch any of the previous environments.

4. Spawn the rover in this environment: 
```
roslaunch fox_gazebo spawn_fox.launch
```

6. Open a new terminal and start teleop: 
```
sudo apt-get install ros-melodic-teleop-twist-keyboard
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
![rover inside a custom environment](https://github.com/dobots/workshops/blob/master/gazebo_environments/images/simple_shapes_rover.png)




