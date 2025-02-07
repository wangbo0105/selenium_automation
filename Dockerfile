#FROM selenium/node-chrome-debug
FROM 820585630/robot

USER root

ENV NODE_MAX_INSTANCES 10
ENV NODE_MAX_SESSION 10
ENV HOME=/automation

WORKDIR ${HOME}


# DEBUG USE
#RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

# install pip3
RUN apt-get update
RUN apt-get install -y python3-pip

# install selenium
#RUN sudo pip3 install selenium robotframework pyperclip # -i https://pypi.douban.com/simple

RUN sudo pip3 install selenium pyperclip # -i https://pypi.douban.com/simple

RUN mkdir -p ${HOME}

RUN chmod 755 ${HOME}

COPY . ${HOME}/

VOLUME  ${HOME}/report

ENTRYPOINT ["./entrypoint.sh"]

