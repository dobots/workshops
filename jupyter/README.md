
# Getting familiar with Jupyter notebook and Jupyter ROS

## Presentation ROS in the Jupyter notebook:
[https://vimeo.com/378683268](https://vimeo.com/378683268)

## Install pip if you don't have already:
```
sudo apt update
# Python2 
sudo apt install python-pip
#or Python3
sudo apt install python3-pip
```

## Install jupyter using pip:
```
pip install jupyter
# or based on your pytho nversion
pip3 install jupyter
```

## Launching First Notebook

To launch a Jupyter notebook, open your terminal and navigate to the directory where you would like to save your notebook. Then type the below command and the program will instantiate a local server at  [http://localhost:8888](http://localhost:8888)

```
jupyter notebook
```

Follow the tutorial on:
(ultimate-beginners-guide-to-jupyter)https://medium.com/velotio-perspectives/the-ultimate-beginners-guide-to-jupyter-notebooks-6b00846ed2af

## Uploading a Jupyter notebook to Github

Github has integrated support for rendering  .ipynb files directly in repositories.
You can follow your usual flow of commiting and pushing the saved notebook to your github repository, and it will be automatically rendered.


## Install interactive widgets: ipywidgets

```
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension
```

## Create a slider

Run `jupyter notebook`, then create a new notebook.
Try the commands used in the `workshops/jupyter/intro_ipywidgets.ipynb`file

## Jupyter-ROS library

Folow the instructions to install it: [jupyter-ros](https://github.com/RoboStack/jupyter-ros)

### Troubleshooting

1. If `jupyter nbextension enable --py --sys-prefix ipywidgets` fails, try to run it without the `--sys-prefix`:
	```
	jupyter nbextension enable --py widgetsnbextension
	```

2. If `jupyter nbextension enable --py --sys-prefix jupyros` fails, try to run it without the `--sys-prefix`:
	```
	jupyter nbextension enable --py jupyros
	```

3. If `jupyter labextension install jupyter-ros` fails, try to install labextension at first:
	```
	pip install jupyterlab
	 ```
	Then run the `jupyter labextension install jupyter-ros` again.

4. If during the 'development installation' running
	 ```
	jupyter nbextension install --py --symlink --sys-prefix jupyros
	jupyter nbextension enable --py --sys-prefix jupyros
	``` 
	returns with an error that permission denied, try to remove the `--sys-prefix` and add 	the `--user` tag.


5. As the official troubleshooting guide points out: You might see a warning like "The rospy package is not found in your $PYTHONPATH. Subscribe and publish are not going to work. Do you need to activate your ROS environment?"
You can should set the path from inside the notebook using:
	```
	import sys
	sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages/')

	# The next line should now work!
	import jupyros
	```
6.  In case you have multiple instances of ROS installed on your system, you might have some problems when importing `rospy` in your notebook.  You need to make sure that your ROS_DISTRO is configured, and your ROS_PATH is set as well in your `~/.bashrc` :
	
	```
	#Source ROS noetic
	source /opt/ros/noetic/setup.bash
	export ROS_DISTRO=noetic
	```

## Installing Zethus

Follow the instructions:
[https://github.com/rapyuta-robotics/zethus](https://github.com/rapyuta-robotics/zethus)

* Clone the repository
	 ```
	 git clone https://github.com/rapyuta-robotics/zethus.git
	 cd zethus
	 ```
 
 * Install npm
	 ```
	sudo apt-get install npm
	```

* Install the package with npm
	```
	npm install
	```

* Run the package:
	```
	npm run build
	```
* In a new terminal create a server:
	```
	npx serve
	```
*In the webbrowser open the localhost link created by npx serve.

* or use docker:
	```
	docker build -t=zethus .
	docker run -p 8080:8080 zethus	
	```


# Start a ROS simulation and connect to it

## Clone the tb3 repo:

```
	git clone git@github.com:dobots/tb3.git
	ln -s git_ws/tb3 catkin_ws/src/tb3
```

## Install ROS-bridge and start Gazebo:

```
sudo apt-get install ros-<rosdistro>-rosbridge-suite
```
 Run the websocket:
 ```
 roslaunch rosbridge_server rosbridge_websocket.launch
 ```
or add websocket to your launch file`tb3_arena_websocket.launch`:
```
<launch>
  <include file="$(find rosbridge_server)/launch/rosbridge_websocket.launch" > 
     <arg name="port" value="9090"/>
  </include>
 </launch> 
  ```


## Start Zethus

In a new terminal run:
```
docker run -p 8080:8080 zethus
```

Open a webbrowser:
```
localhost:8080
```
Configure the ROS Endpoint:
```
ws://0.0.0.0:9090
```


## Conclusions

* Jupyter notebooks are useful tools when you would like to create some python based graphs, documentations and shared or present it to others

* Jupyter-ROS is has many dependencies and errors. It can be frustrating to set it up and therefore, complicated to share with others. Possible solution could be to create a Docker image.

* The installation of Zethus is not documented properly, it can be challenging to install. After installation it still crashes whenever we would like to edit the configurations. Our conclusion is to explore other web-based RViz tools, which might be more user friendly or easier to share with others.




