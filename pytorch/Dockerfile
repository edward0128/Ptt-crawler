FROM pytorch/pytorch:latest
RUN sed -i 's/archive.ubuntu.com/free.nchc.org.tw/g' /etc/apt/sources.list
  
RUN apt update && apt install wget -y
RUN echo deb http://deb.obspy.org xenial main >> /etc/apt/sources.list
RUN wget --quiet -O - https://raw.github.com/obspy/obspy/master/misc/debian/public.key | apt-key add - 
RUN apt update
  
#RUN apt install -y openssh-server

RUN apt install -y openssh-server python3-obspy -y
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
  
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
#RUN pip3 install --upgrade pip
#RUN apt-get install -y python3-pip
#RUN pip3 install jupyter
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install jupyter

RUN conda install -c anaconda cudatoolkit==9.0
RUN pip uninstall torchvision
RUN pip install torchvision==0.2.2

EXPOSE 8888
EXPOSE 22
COPY my_wrapper_script.sh my_wrapper_script.sh
COPY .jupyter /root/.jupyter
COPY examples /home/examples

#COPY tensorflow-for-poets-2 /home/tensorflow-for-poets-2 
#COPY Training_flower_demo.ipynb /home/Training_flower_demo.ipynb
# setting password ssh and jupyter
CMD ./my_wrapper_script.sh $password
