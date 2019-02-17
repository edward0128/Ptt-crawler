# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jupyter Project <jupyter@googlegroups.com>"

USER root

# Install Tensorflow
RUN conda install --quiet --yes \
    'tensorflow=1.12*' \
    'keras=2.2*' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER
#######################################################
RUN apt-get update && apt-get install -y openssh-server && apt-get install -y vim
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
 
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd 
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
#######################################################
RUN pip install requests requests_html
RUN pip install lxml
#######################################################
EXPOSE 22
EXPOSE 8888
#######################################################

#CMD service sshd start && service nginx start

#CMD ["sh","-c","service sshd start && nginx -g daemon off"]
#RUN sh -c "service sshd start"
#CMD ["nginx", "-g", "daemon off;"]

COPY my_wrapper_script.sh my_wrapper_script.sh
CMD ./my_wrapper_script.sh
