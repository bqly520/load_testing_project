# Load Testing Project

The objective of this project was to build an "API" that returns current date/time in a JSON format. Additionally, there will be a test application which queries the "API" X times per second which will record `success`, `failure`, `and TTLB(Time to Last Byte)`.

### Different Sections
- [Instructions to run Web Application](#instructions-to-run-web-application)
- [Docker Learning](#docker-learning)
- [Python Libraries](#python-libraries)
    - [CherryPy](#cherrypy)
    - [Requests](#requests)

### Instructions to run Web Application

1. Clone the repository to your local system and change directory into the project
```bash
git clone https://github.com/bqly520/load_testing_project.git
cd load_testing_project
```

2. Assuming that you already have Docker CLI installed, run the following command.
```bash
# This command will first read the docker file and build the images
# Then it will create and run two containers once they are ready
# Note: the containers will both be created into a network called 'load_testing_project_default'
docker-compose up
# Can possibly go into more details about the Dockerfile maybe...?
```

3. Once the containers are running, you can navigate to the [Date-Time Web Application](http://localhost:7777/date) and verify that the return object is of JSON format. You can validate by inspecting the page and checking to see if the `Content-Type: application/json`.
![Web-App](date-time-application-sc.png)

4. Example of using the test application (with screenshots) Navigate to http://localhost:8888/, will need to click back

5. `Caution:` Please do not run code seperately because even though both application are accessible, the test will fail because the container name is able to resolve the DNS since both containers are within the user-defined network. This capability is called `automatic service discovery`.

6. Takeaways(?) TBC....

### Docker Learning
```bash
# Building the docker image with a tag 'date-api'
docker build -t date-api .

# Run the docker image, -d(detaching) for running in the background
docker run -d -p 7777:7777 date-api

# Configuring multiple containers at the same time
docker-compose up

# List images
docker images

# Docker inspect displays loads of details on the resource
docker inspect <network> <container> <image>

# Remove images
docker rmi Image Image

# List containers
docker ps -a

# Remove containers
docker rm ID_or_Name

# Build one or many images,
docker-compose build
```

#### docker-compose
This file is basically the backbone of Docker-Compose as it contains all the information needed to run the desired services. These services can pretty much be anything you want, in this example I’ll only be running a container for the app itself and another container for the test app, but you could also have other services.


### Python Libraries

### CherryPy
CherryPy allows developers to build web applications in much the same way they would build any other object-oriented Python program. This results in smaller source code developed in less time.
```bash
pip install CherryPy
```