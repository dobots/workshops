# Julia workshop #

### Setup Julia ###

**Basic setup**

* Julia can be downloaded and installed in Linux with the use of a package manager known as ‘Snaps’. Follow the steps given below to install Snaps and Julia in a Linux system using command-line:
	```
	sudo apt install snapd
	```

* Install Julia: 
	```
	sudo snap install julia --classic
	```

* Run Julia: 
	```
	julia
	```

**Extra Information**
* After starting julia, enter ] in the command line to use the build in package manager (https://docs.julialang.org/en/v1/stdlib/Pkg/index.html) and leave the package manager with a backspace to enter the julia prompt again 

* For example (may takes a few minutes): 
	```
	1. julia
	2. ]
	3. add IJulia Plots CSV DataFrames
	4. using IJulia
	5. notebook()
	```

* Do: ] --> package manager
* Do: ? --> help
* Do: ; --> shell
* Do: backspace --> back to Julia 


### Practice ###

**Hello World**
* Leave Julia 
* Go to Julia_workshop
* Make a new file called hello_world.jl:
	```
	nano hello_world.jl
	```
* Add the following to the file: 
	```
	#Julia program to print Hellow World

	println("Hello World!") 
	```
* Put in the following command: 
	```
	julia hello_world.jl
	```
* This should print: Hello World! 

### Tutorial ###
**Introduction video**
* https://www.youtube.com/watch?v=qhrY0c_BHs8 (start at: 3:54) 

**Explanation coding**
* https://www.youtube.com/watch?v=Cj6bjqS5otM (start at: 10:40) 

**Julia Acedemy**
* This is a free Julia course (All the files are on github already) 
* This is the website with explanation videos: https://juliaacademy.com/courses/375479/lectures/5815852

### Docker ###

Maybe it is nice to try Julia in Docker. I have tried this, but I didn't manage to do it. Maybe this is a nice practice

* get docker image: https://hub.docker.com/_/julia
* Do:
	```
	docker image list
	```
	
* Create Dockerfile: 
	```
	FROM julia:latest
	....? 
	```

* Create run.sh file: 





