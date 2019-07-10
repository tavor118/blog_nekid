# Pull base image
FROM python:3.6

# Upgrade pip
RUN python -m pip install --upgrade pip

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /src

# Set the working directory to /src
WORKDIR /src

# Copy the current directory contents into the container at /src
COPY ./blog_ne_kid /src/

ADD requirements.txt /src/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt