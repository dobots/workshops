
# Getting familiar with Jupyter notebook and creating RViz in it

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

To launch a Jupyter notebook, open your terminal and navigate to the directory where you would like to save your notebook. Then type the below command and the program will instantiate a local server at  [http://localhost:8888/tree.](http://localhost:8888/tree.)

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

Run `jupyter notebook`, the ncreate new notebook.
Try the commands used in the `intro_ipywidgets.ipynb`file

## Jupyter-ROS library

Folow the instructisons to install it:
[jupyter-ros](https://github.com/RoboStack/jupyter-ros)


## Jupyter amphion demo


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
*In the webbrowser open the localhost lin kcreated by npx serve.

* Running with docker:
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

## Open a webbrowser:
```
localhost:8080
```
ROS Endpoint:
```
ws://0.0.0.0:9090
```







