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

# expose flask port
EXPOSE 5000