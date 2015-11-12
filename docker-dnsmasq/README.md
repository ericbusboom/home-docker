
# docker-dnsmasq



## Build

    docker build -t ericbusboom/dns .


## Run

    docker run -d -p 53:53/udp -p 8081:8080 --name dns ericbusboom/dns 

