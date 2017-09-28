
# docker-dnsmasq


## Running on QNAP nas

The QPAN container server runs a DHCP server, which conflicts with the one in this container. 

This command seems to stop the daemon:

    daemon_mgr  dhcpd_lxcbr0 stop "/mnt/ext/opt/netmgr/api/core/dhcpdLink/dhcpd_lxcbr0 -cf /etc/dhcpd_lxcbr0.conf -lf /var/state/dhcp/dhcpd_lxcbr0.leases -pf /mnt/ext/opt/netmgr/api/core/dhcpdLink/lxcbr0.pid"


## Build

    docker build -t ericbusboom/dns .


## Run

First, create a network

    docker network create --subnet=192.168.0.0/21 local_net

Then run

    docker run -d -p 53:53/udp -p 8081:8080 --name dns ericbusboom/dns 

Or, more likely, run 

    make start
