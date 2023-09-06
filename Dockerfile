# Set base image (host OS)
FROM python:3.8-alpine
# set environment variable
ENV LINE_CHANNEL_ACCESS_TOKEN=BeYPpX123W8rlneAOQaPhvbTPegaN9YFnnLZg8D5lfyw9L4EMYpa9wX/2iZ64vfDq7yz/OLHN1rnlWEVNg9I2oBZnpVO/vSc8RcdXSWMdWaRFZqU7CyUVyuqYtMdDjB/dMopEtxHu0ala3l7eLkrlwdB04t89/1O/w1cDnyilFU=
ENV LINE_CHANNEL_SECRET=74151448926e1a4b2532532469237663
ENV OPENAI_API_KEY=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
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
