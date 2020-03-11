
FROM ubuntu

MAINTAINER eric@busboom.org

RUN apt-get update && \ 
apt-get upgrade -y && \
apt-get install -y wget curl git  && \
apt-get clean && rm -r /var/lib/apt/lists/*

ADD nginx.tmpl /etc/docker-gen/templates/nginx.tmpl

CMD bash