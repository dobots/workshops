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

## ROS noetic tf docker 
This docker is setup to work with tensorflow, ROS noetic, and Openai Gym:

	```
	https://gym.openai.com/
	https://gym.openai.com/envs/#classic_control
	```

1. Add the docker files to your docker folder, and move to the folder:
	
2. Build this docker image in the same folder: 
	 ```
	docker build -t ros_noetic_tf .
	```
3. Copy the tf2RL.py script to a project folder:
	```
	mv tf2RL.py ~/projects/tensorflow 
	```

4. Move to the projects folder, and run the script to enter the container: 
	
	```
	cd ~/projects
	./run.sh
	```


### TF tutorial Actor-Critic
The tutorial can be found at:

	```
	https://www.tensorflow.org/tutorials/reinforcement_learning/actor_critic
	```

1. Change the optimizer in line 27

2. Adjust the number of hidden neurons line 44

3. Add an extra dense layer behind the common layer. 

4. Move to the evaluate the ```train_step``` function





