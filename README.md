# Docker Container: Docker_GoogleTranslate
This is the second individual project for ECE 590: Data Analysis at Scale in the Cloud. 
<br> In this project, I build a docker container with a python script that can translate texts in any language into Enligsh in AWS Cloud9 that uses the official Python base image. I also use circleci for continuous integration.

### Docker Image
The docker image for this project can be found [here](https://hub.docker.com/r/wh132/docker_googletranslate).

### Run the Docker Image
* Open your terminal or Cloud9 environment
* Run the command `docker pull wh132/docker_googletranslate`
* Run the command  `docker run -it wh132/docker_googletranslate bash` for creating a bash environment with the docker image.
* Run the command `python app.py`
* Follow the instruction to complete the translation.

### Video Demo
Vide demo can be found [here](www.youtube.com)
