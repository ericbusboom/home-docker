
NS = civicknowledge.com
VERSION = latest

REPO = docker-hello-world
NAME = docker-hello-world
INSTANCE = default
DOCKER ?= docker

PORTS= --network=webproxy

ENV =  \
    -e VIRTUAL_HOST=hello.civicknowledge.com  \
    -e LETSENCRYPT_HOST=hello.civicknowledge.com \
    -e LETSENCRYPT_EMAIL=eric@civicknowledge.com 

.PHONY: build push shell run start stop restart reload rm rmf release

build:
	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .

push:
	$(DOCKER) push $(NS)/$(REPO):$(VERSION)

shell:
	$(DOCKER) run --rm -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) 

attach:
	$(DOCKER) exec  -ti $(NAME) /bin/bash

run:
	$(DOCKER) run --rm --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

logs:
	$(DOCKER) logs -f $(NAME) 

start:
	$(DOCKER) run -d --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

stop:
	$(DOCKER) stop $(NAME)
	
restart: stop rm start

reload: build rmf start

rmf:
	$(DOCKER) rm -f $(NAME)

rm:
	$(DOCKER) rm $(NAME)

release: build
	make push -e VERSION=$(VERSION)

default: build