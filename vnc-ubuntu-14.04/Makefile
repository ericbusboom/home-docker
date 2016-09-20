
INSTANCE = default
DOCKER ?= docker

NS = dorowu
VERSION = latest

REPO = ubuntu-desktop-lxde-vnc
NAME = ubuntu-desktop-lxde-vnc

DOCKER ?= docker

FLASK_APP ?= start.py

PORTS =  -p 6080:6080

#VOLUMES= -v /share/CACHEDEV1_DATA/docker/docker-fs:/var/docker-fs

# ENV = -e VIRTUAL_HOST=devel.busboom.org -e FLASK_APP=$(FLASK_APP) -e FLASK_DEBUG=1

.PHONY: build push shell run start stop restart reload rm rmf release

build:
	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .

push:
	$(DOCKER) push $(NS)/$(REPO):$(VERSION)

shell:
	$(DOCKER) run --rm --name $(NAME) -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) /bin/bash

run:
	$(DOCKER) run --rm --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

logs:
	$(DOCKER) logs -f $(NAME) 

start:
	$(DOCKER) run -d --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

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