# ROS2

Major changes from ROS1:

- No ROS master. Nodes communnicate using a DDS bus connecting everything. A lot of flexibility and reliablity in terms of communication framework.
<p align="center">
  <img height="350" src="https://www.electronicspecifier.com/cms/images/RTI_figure7_Autonomous_Cars1.jpg" >
</p>

- With no dedicated master, this also means that ROS2 does not have any global parameter space as was the case in ROS1

- Much better python support. Python3 use by default. Has new ROS Python packages as an alternative to CMake.

- Launch files are mainly in python for most packages, though support for xml based launch files has slowly been added back.

- LifeCycle Nodes. Node functionality can be extended to include a state-machine within the node. This is useful for example in Navigation packages to ensure all localization, navigation components are in the right state.

# Useful commands:

## General:

(**Note**:Install python3-argcomplete for autocompletion)

ros2 node list

ros2 service list

ros2 service find <msg_type>

ros2 action list

ros2 param get/set <node_name> <parameter_name> <value>

ros2 param dump /turtlesim (Saving to:  ./turtlesim.yaml)

ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: -1.57}" --feedback

### Topic Info:
ros2 topic list -t

ros2 topic pub --rate 1/--once <topic_name> <msg_type> '<args>'

ros2 topic hz /turtle1/pose

ros2 topic type /turtle1/pose

### Get message format info:
ros2 interface show geometry_msgs/msg/Twist

### Remap parameter and launch node:
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel

ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle

### Get params from file and run node:
ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>

### Bag files
ros2 bag record -o <file_name> <topic_name1> <topic_name2>


## Build System:

### Create package
ros2 pkg create --build-type ament_cmake <package_name>

ros2 pkg create --build-type ament_python <package_name>

(Optional: add --dependencies:)

ros2 pkg create --build-type ament_cmake cpp_srvcli --dependencies rclcpp example_interfaces

### Check executables in a package:
ros2 pkg executables turtlesim

### Install dependencies
rosdep install -i --from-path <ws_path>/src --rosdistro eloquent -y

**Note**: For the error "Cannot locate rosdep definition for [ament_python]", remove "<buildtool_depend>ament_python" in **package.xml**

### Build:
colcon build

colcon build --packages-select my_package

### Source:
source /opt/ros/eloquent/setup.bash
source <ws_path>/install/local_setup.bash

(Optional source colcon_cd)
source /usr/share/colcon_cd/function/colcon_cd.sh

## Migrating launch files from ROS1 to ROS2:

### Add following code to have ros2 recognize/use additional files in your package (added to the 'share' directory):
#### Cmake package: to the package CMakeLists file:
install(DIRECTORY
  launch
  urdf
  meshes
  rviz
  DESTINATION share/${PROJECT_NAME}/
)
#### Python package: to the setup.py file in data_files:
(os.path.join('share', package_name), glob('launch/*.launch.*')),
(os.path.join('share', package_name), glob('urdf/*'))

### Aditional executable scripts (Eg. ros2 run <pkg> <executable>.py) need to be added to the package 'lib' directory and can be done adding the following code:
#### Cmake package: to the package CMakeLists file (if in scripts/ folder):
#### (NOTE: This is the easiest way to add python ros code to your CMake package)
install(PROGRAMS 
  scripts/demo.py
  DESTINATION lib/${PROJECT_NAME}/
)

#### Python package: to the setup.py file in data_files:
(os.path.join('lib', package_name), glob('scripts/*')),

### Get all the launch packages
sudo apt install ros-<distro>-launch*

### No more global params. Have to be declared for every node. Eg:
<node pkg="robot_state_publisher" exec="robot_state_publisher" name="robot_state_publisher">
        <param name="robot_description" command="$(find xacro)/xacro --inorder $(find-pkg-share tb3_description)/urdf/turtlebot3_waffle_base.urdf.xacro" />
</node>

### 'type' is now 'exec'

### 'find'
In launch.xml files, 'find' is now 'find-pkg-share' for the share directory and 'find-pkg-prefix' is for the install directory. To get to the actual package location you could /../../src/pckg_name/ OR the proper way would be to share the files you need using the CMakelists file (see above).

In urdf files, 'find' is still used and points to the share directory.

### Gazebo
Spawning requires latest version of gazebo9!
Make sure Gazebo can replace paths such as package:// from the urdf! To do this add to the package.xml (of tb3_description for Eg.):
<gazebo_ros gazebo_model_path="${prefix}/../"/>

## Troubleshooting:

### Substitutions in launch.xml
Some of the partial substitutions (Eg. $(sub)/abc/xyz.rviz) don't work well when used in `args`. An alternative is to define a separate variable and substitute that in `args` (Eg. A variable `rviz_cfg_path` is defined in `fox_gazebo/launch/gazebo.launch.xml` and then this variable is used in `args` when launching rviz at the end of the launch file).

### On ros2-eloquent, in order to run Navigation2, BehaviorTree.CPP is required to be built from source (https://github.com/BehaviorTree/BehaviorTree.CPP/tree/ros2-devel)
https://github.com/ros-planning/navigation2/issues/1948

### LifeCyle nodes in Navigation2
All nodes in Navigation2 are LifeCycle nodes and thus need to be in the right state to function properly. You could use the Navigation2 tool (panel) in rviz to pause/reset these lifecycle nodes correctly.

### LaserScan not visible
In Rviz, the 'Reliability' setting for the LaserScan has to be changed to 'Best Effort' for rviz to visualize Laser Scans.

# ROS1to2 Bridge:
Steps to use:
### 1. clone the repository
https://github.com/ros2/ros1_bridge (Choose the branch as per your ROS distro)

### 2. In the ROS2 workspace, build everything but the ROS 1 bridge
colcon build --symlink-install --packages-skip ros1_bridge

### 3. source all ROS 1 and then ROS 2 environments and workspaces
source /opt/ros/melodic/setup.bash
source ~/DoBots_WS/tb3_ws/devel/setup.bash

source /opt/ros/eloquent/setup.bash
source /home/sjauhri/DoBots_WS/tb3_ros2_ws/install/local_setup.bash

### 4. In the ROS2 workspace, build the ROS1 bridge
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure

## Troubleshooting:
- Install turtlebot3_msgs
- ros1_bridge takes a looong time to build. Consider putting it somewhere else