# Pull a prebuild docker image
FROM python:3.8.1-slim-buster

# Setup a work directory
WORKDIR /code

# copy the pip requirements
COPY config/requirements.txt /code/requirements.txt

# upgrade pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r /code/requirements.txt

# make a directory
RUN mkdir -p /usr/share/man/man1 

# install java
RUN apt update --assume-yes
RUN apt upgrade --assume-yes
RUN apt install default-jre --assume-yes

# expose flask port
EXPOSE 5000