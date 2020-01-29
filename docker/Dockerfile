FROM ubuntu:18.04
MAINTAINER Dax Mickelson (dmickels@cisco.com)

# Configure Script and GIT variables
ENV WORK_DIR /usr/src/app
WORKDIR $WORK_DIR
ENV PYTHON_SCRIPT bootstrap.py

# Running APT UPDATE
RUN apt-get -y update

# Install APT-UTILS
RUN apt-get install -y apt-utils

# Running APT DIST-UPGRADE
RUN apt-get -y dist-upgrade

# Running APT AUTOREMOVE
RUN apt-get -y autoremove

# Running APT AUTOCLEAN
RUN apt-get -y autoclean

# Install Python modules
RUN apt-get -y install python3 python3-pip

# Install git
RUN apt-get install -y git

# Install Python modules needed for this script.
COPY requirements.txt $WORK_DIR
RUN python3 -m pip install --no-cache-dir -r $WORK_DIR/requirements.txt

# Provide some examples in case the user doesn't mount their own script dir.
COPY example_scripts $WORK_DIR

# Copy over bootstrap file
COPY bootstrap.py $WORK_DIR

# Run script.
CMD python3 $WORK_DIR/$PYTHON_SCRIPT
