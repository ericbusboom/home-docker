# Originally from: https://github.com/jpillora/docker-dnsmasq

FROM phusion/baseimage:latest

MAINTAINER eric@busboom.org

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -y python ca-certificates curl && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*
    
#RUN mkdir /etc/service/dnsmasq
#ADD dnsmasq.sh /etc/service/dnsmasq/run

CMD ["/sbin/my_init"]

#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*