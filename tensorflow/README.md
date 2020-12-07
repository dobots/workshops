#  Tensorflow Worshop
You can run tensorflow tutorials directly in the browser, or from your local workstation. 

## Websites
To go souces. 
* Tensorflow installation: 
	```
	https://www.tensorflow.org/install
	```
* Tensorflow API documentation:
	```
	https://www.tensorflow.org/api_docs
	```
* Tensorflow tutorials:
	```
	https://www.tensorflow.org/tutorials
	```
## Simple classification tutorial
* The tutorial is online at: 
```
https://www.tensorflow.org/tutorials/keras/classification
```
* pull the latest tf docker for simple tutorials

	```
	docker pull tensorflow/tensorflow:latest
	```
* run the jupyter notebook
	
	```
	docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter
	```

## ROS noetic tf docker 
This docker is setup to work with tensorflow, ROS noetic, and Openai Gym:

	```
	https://gym.openai.com/
	https://gym.openai.com/envs/#classic_control
	```

1. Add the docker files to your docker folder, and move to the folder:
	```
	cp -r ros_noetic_tf ~/dockers/ros_noetic_tf
	cd ~/dockers/ros_noetic_tf
	```
	
2. Build this docker image in the same folder: 
	```
	docker build -t ros_noetic_tf .
	```

3. Copy the tf2RL.py script to your projects folder:
	```
	mv tf2RL.py ~/projects/
	```

4. Move to the projects folder, and run the docker script to enter the container: 
	
	```
	cd ~/projects
	~/dockers/ros_noetic_tf/run.sh
	```


### TF tutorial Actor-Critic
The tutorial can be found at:
	```
	https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic
	```

1. Move to the project folder:
	```
	cd ~/projects/tensorflow
	```
2. Run the tutorial python script:
	```
	Python3 tf_RL.py
	```
	
2. Change the optimizer in line 27

3. Adjust the number of hidden neurons line 44

4. Add an extra dense layer behind the common layer. 

5. Move to the evaluate the ```train_step``` function





