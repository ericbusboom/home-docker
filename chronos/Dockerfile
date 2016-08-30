# Originally from: https://github.com/jpillora/docker-dnsmasq

FROM phusion/baseimage:0.9.17

MAINTAINER eric@busboom.org

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    gcc git curl python python-dev python-pip \
    libyaml-dev at \
    && \
	apt-get autoremove -y && \
	rm -rf /var/lib/apt/lists/*
 
RUN pip install -U "git+https://github.com/ericbusboom/insteon.git#egg=insteon"
    

ADD insteon.cron /etc/cron.d/insteon.cron
ADD insteon.yaml /etc/

#RUN mkdir /etc/service/chronos
#ADD run/chronos.sh /etc/service/chronos/run
    
CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp
