# Originally from: https://github.com/jpillora/docker-dnsmasq

FROM phusion/baseimage:0.9.17

MAINTAINER eric@busboom.org

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -y dnsmasq ca-certificates curl && \
	apt-get remove --purge -y curl && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*
    
RUN echo -e "ENABLED=1\nIGNORE_RESOLVCONF=yes" > /etc/default/dnsmasq

COPY dnsmasq.conf /etc/dnsmasq.conf

COPY dns-entries.conf /etc/dnsmasq.d/dns-entries.conf 

# Docker /etc/hosts files are basically read-only
COPY hosts /etc/dnsmasq.d/hosts

CMD dnsmasq -d -h -H /etc/dnsmasq.d/hosts