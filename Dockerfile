FROM selenium/node-chrome-debug

ENV HOME=/automation

# install pip3
RUN sudo apt-get update
RUN sudo apt-get install -y python3-pip

# set display port to avoid crash
#ENV DISPLAY=:99
ENV NODE_MAX_INSTANCES 10
ENV NODE_MAX_SESSION 10

# install selenium
RUN sudo pip3 install selenium robotframework


RUN sudo mkdir -p ${HOME}

RUN sudo chmod 755 ${HOME}

RUN sudo chmod 755 ${HOME}/entrypoint.sh

WORKDIR ${HOME}

COPY . ${HOME}/

ENTRYPOINT ['sh', '${HOME}/entrypoint.sh']


