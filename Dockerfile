# Use an official Python runtime as a parent image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    git python3.10 python3.10-venv python3.10-dev python3-pip \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s /usr/bin/python3.10 /usr/bin/python

RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install PADE manually as described in the README
RUN mkdir lib && \
    cd lib && \
    git clone https://github.com/alvarocaboUPM/pade
RUN cd lib/pade && \
    python3 setup.py install && \
    cd ../../ && \
    rm -rf lib

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the application will run on
EXPOSE 20000

# Run the application
CMD ["pade", "start-runtime", "--port", "20000", "--username", "test", "--password", "test", "src/pub_sub_agent.py"]
