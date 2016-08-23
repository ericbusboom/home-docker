
# docker-dnsmasq



## Build

    docker build -t ericbusboom/dns .


## Run

    docker run -d -p 53:53/udp -p 8081:8080 --name dns ericbusboom/dns 


## Makefile.local

THe Makefile expects an include file, Makefile.local, which has local config values. 

    PORTS = -p 8080:80

    VOLUMES = -v /var/log/docker:/var/log

    ENV = \
      -e SOME_KEY=SOME_VALUE


This file is excluded from git