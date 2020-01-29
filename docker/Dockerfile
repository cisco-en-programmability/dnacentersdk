FROM dmickels/dnacentersdk:latest
MAINTAINER Dax Mickelson (dmickels@cisco.com)

# Configure Script and GIT variables
ENV WORK_DIR /usr/src/app
WORKDIR $WORK_DIR
ENV PYTHON_SCRIPT bootstrap.py

# Provide some examples in case the user doesn't mount their own script dir.
COPY example_scripts $WORK_DIR

# Install Python modules needed for this script.
RUN python3 -m pip install --no-cache-dir -r $SCRIPT_PATH/requirements.txt

# Run script.
CMD python3 $WORK_DIR/$PYTHON_SCRIPT
