Dependencies:
ros-melodic-full docker image 
or
ros-melodic installation with Gazebo

blender installation


 

I. Part of the workshop creating custom Gazebo environments

1. Create a gazebo_environments_ws/src folder

2. Copy the content simple_shapes_description folder from this folder into your workspace src folder.
Doesn't create a symbolic link, because Docker doesn't like them ;)

3. Start gazebo and insert models - save as - just show how does it work

3. Walk through the files, explain each part


4. Copy this folder, give a new name and start editing

5. Open CMakeLists.txt and change the project name to the name of the folder

6. Open package.xml and change the project name to the name of the folder, edit the description tag, fill in your email, choose license ( by default BSD). Add tag to the end of the file to automatically add these models to the gazebo_plugin_path.

7. Update the Readme file

8. Rename your world file

9. Rename and edit your launch file

10. Create a meshes folder in your ros package ( now you should have launch, meshes, worlds folders)



11. Dowload a mesh file (https://www.thingiverse.com/ or any other platform. Look for .stl or .dae (collada) files.
.stl files can be opened and converted to .dae in blender. To be able to add materials and different colours.





7. Put the .dae or .stl file inside your meshes folder
 - for collision a simplified model can be used
 -if you would like to use one colour you can add it here



6. Open in blender if you would like to edit the file, or colour different parts to different colours. The new blender had a bug for a while, that the colours were not saved properly. The old blender 2.x can save it properly.



7. Edit your world file:
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

8. Run catkin_make, source devel/setup.bash

9. Launch your world






II. Part of the workshop - importing 3D map in Gazebo

## Converting 3D models from OpenStreetMap to .stl format

 1.   Select the region of interest in Open Street Map and Export it
		 - Go to the website  [Open Street Map](http://www.openstreetmap.org/).
   
	  - Click the  **Export**  button at the top of the screen.

	  - Fill in the latitude and longitude coordinate range (scroll through the coordinate fields by pressing a  **Tab**  key to view an area on the map).
	  -  Click the  **Export**  button the left side of the screen (the file extension will be  _.osm_).

 2. Map editing
	- Visit the site  _https://josm.openstreetmap.de/wiki/Download_  to download the  JOSM  application  _josm-tested.jar_.

	- Open an application with the command: 

	 	 `java -jar josm-tested.jar`
	If you don't hava java installed, install java-8 !!! Do not install openjdk-11! It has some bugs and the 3D map creation won't work! 

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
	- Documentation:  _http://www.openscenegraph.org/index.php/documentation/guides/user-guides/55-osgconv_
	
	- Install open scene graph:
		`sudo apt install openscenegraph`

	- Run the command:
	
		`osgconv map_pucrs.obj map_pucrs.stl`


[Converting 3D models from OpenStreetMap to .stl format copied from: https://pucrs-campus-on-gazebo.readthedocs.io/en/latest/source/campus/](https://pucrs-campus-on-gazebo.readthedocs.io/en/latest/source/campus/)


## Create a package with the new .stl file

1. Copy the simple_shapes_mesh_description folder, give a new name and start editing

5. Open CMakeLists.txt and change the project name to the name of the folder

6. Open package.xml and change the project name to the name of the folder, edit the description tag, fill in your email, choose license ( by default BSD). Add tag to the end of the file to automatically add these models to the gazebo_plugin_path.

7. Update the Readme file

8. Rename your world file

9. Rename and edit your launch file

10. Put the previously created mesh file into your meshes folder
 - for collision a simplified model can be used
 -if you would like to use one colour you can add it here

6. Open in blender if you would like to edit the file, or colour different parts to different colours. The new blender had a bug for a while, that the colours were not saved properly. The old blender 2.x can save it properly.



7. Edit your world file. Remove the simple shapes and the change the mesh file description to this new mesh file:
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

8. Run catkin_make, source devel/setup.bash

9. Launch your world - use just a couple of buildings, otherwise Gazebo might crash! You might need to edit the files in blender to simplify the meshes.









III.Part - spawn a rover

1. Copy the rover description folder - walk through the included files

2. Copy the rover_gazebo folder - spawn the rover in your environment

3. Start teleop





