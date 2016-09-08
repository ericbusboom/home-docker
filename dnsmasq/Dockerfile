# Originally from: https://github.com/jpillora/docker-dnsmasq

FROM phusion/baseimage:latest

MAINTAINER eric@busboom.org

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -y python dnsmasq ca-certificates curl && \
	apt-get remove --purge -y curl && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*
    
RUN echo -e "ENABLED=1\nIGNORE_RESOLVCONF=yes" > /etc/default/dnsmasq

COPY convert-hosts.py /tmp/convert-hosts.py
COPY hosts /etc/dnsmasq.d/hosts 
COPY dnsmasq.conf /etc/dnsmasq.conf
#COPY dns-entries.conf /etc/dnsmasq.d/dns-entries.conf 
COPY dnsmasq.local.conf /etc/dnsmasq.d/dnsmasq.local.conf

RUN python /tmp/convert-hosts.py > /etc/dnsmasq.d/dns-entries.conf 

RUN mkdir /etc/service/dnsmasq
ADD dnsmasq.sh /etc/service/dnsmasq/run

CMD ["/sbin/my_init"]

#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*