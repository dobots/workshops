# Object Oriented Programming Using Python


## Part 1 - OOPs Overview
Most of the code has been derived from [https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc](Corey Schafer Youtube)

1. Navigate to the *.ipynb* file directory and open the jupyter notebook:- 
```
jupyter notebook
```
2. Open the *Python_OOPs.ipynb* notebook 


## Part 2 - OOPs in ROS Overview
In this segment, the way OOPs can be utilised in simple ROS programs has been shown. Most of the code has been taken from [https://roboticsbackend.com/oop-with-ros-in-python/] (OOP with ROS in Python)

### To open the notebook:-

1. Navigate to the *.ipynb* file directory and open the jupyter notebook:- 
```
jupyter notebook
```
2. Open the *Python_OOPs_ROS.ipynb* notebook

### ROS run:-

1. Navigate to a suitable location
2. Create a workspace
```
mkdir -p python_oops/src
cd python_oops/
catkin_make
```
3. Create a package
```
cd src
catkin_create_pkg python_counter std_msgs rospy roscpp
cd ..
catkin_make
```
4. Copy the contents of the python_counter folder to the python_oops/src/python_counter directory
```
cd src/python_counter/
```
5. Run catkin_make
```
cd ../..
catkin_make
```
6. Run the package specific devel script
```
source devel/setup.bash
```
7. Execute the counter with a single counter (without OOPs)
```
roslaunch python_counter counter_launcher.launch
```
To reset the counter, open another terminal and launch:-
```
rosservice call /reset_counter 1
```
8. Execute the counter with a single counter (with OOPs)
```
roslaunch python_counter counter_launcher_oops.launch
```
To reset the counter, open another terminal and launch:-
```
rosservice call /reset_counter 1
```
9. Execute the counter with a multiple counters (with OOPs)
```
roslaunch python_counter counter_launcher_mul_oops.launch
```
To reset the counter, open another terminal and launch:-
```
rosservice call /reset_counter 1
rosservice call /reset_counter_twice 1
```