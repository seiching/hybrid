# Set base image (host OS)
FROM python:3.8-alpine
# set environment variable
ENV LINE_CHANNEL_ACCESS_TOKEN= 
ENV LINE_CHANNEL_SECRET= 
ENV OPENAI_API_KEY= 
# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY *.py .

# Specify the command to run on container start
CMD [ "python", "./main.py" ]
