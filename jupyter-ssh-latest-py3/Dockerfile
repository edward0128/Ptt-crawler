FROM tensorflow/tensorflow:latest-py3
RUN sed -i 's/archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list
  
RUN apt update && apt install wget -y
RUN echo deb http://deb.obspy.org xenial main >> /etc/apt/sources.list
RUN wget --quiet -O - https://raw.github.com/obspy/obspy/master/misc/debian/public.key | apt-key add - 
RUN apt update
  
RUN apt install -y openssh-server python3-obspy -y
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
  
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN pip3 install --upgrade pip
RUN pip3 install jupyter

EXPOSE 8888
EXPOSE 22
COPY my_wrapper_script.sh my_wrapper_script.sh
CMD ./my_wrapper_script.sh $password
  
#EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D"]
