# Controller for control of home docker hosts. 

FROM 32bit/ubuntu:14.04

RUN apt-get update && \
    apt-get install -y openssh-server && \
    sh -c "echo deb https://get.docker.io/ubuntu docker main " > /etc/apt/sources.list.d/docker.list && \
    apt-get update && sudo apt-get install docker.io && \
	apt-get remove --purge -y curl && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*
    
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]