
NS = busboom.org
VERSION = latest

REPO = dnsmasq
NAME = dnsmasq
INSTANCE = default
DOCKER ?= docker
CAP = --cap-add=NET_ADMIN

PORTS177 = -p 192.168.1.177:53:53/tcp -p 192.168.1.177:53:53/udp
PORTS178 = -p 192.168.1.178:53:53/tcp -p 192.168.1.178:53:53/udp


.PHONY: build push shell run start stop restart reload rm rmf release

build:
	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .

push:
	$(DOCKER) push $(NS)/$(REPO):$(VERSION)

shell:
	$(DOCKER) run --rm -i -t $(CAP) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/bash

attach:
	$(DOCKER) exec  -ti $(NAME) /bin/bash

run:
	$(DOCKER) run --rm --name $(NAME) $(PORTS) $(CAP) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

logs:
	$(DOCKER) logs -f $(NAME) 

start177:
	$(DOCKER) run -d --name $(NAME) $(PORTS177) $(CAP) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)


start178:
	$(DOCKER) run -d --name $(NAME) $(PORTS178) $(CAP) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

start:
	@echo Run make start177 or make start178

stop:
	$(DOCKER) stop $(NAME)
	
restart: stop start

reload: build rmf start

rmf:
	$(DOCKER) rm -f $(NAME)

rm:
	$(DOCKER) rm $(NAME)

release: build
	make push -e VERSION=$(VERSION)

default: build