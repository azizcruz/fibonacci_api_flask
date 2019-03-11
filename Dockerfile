FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python3-pip python3
RUN apt-get upgrade python3

# Add source files
COPY . /app
ENV HOME=/app
WORKDIR /app

# Install python dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

ENTRYPOINT ['0.0.0.0:5000']