NS = busboom.org
VERSION = latest

REPO = proxy
NAME = proxy

DOCKER ?= docker

PORTS =   -p 8091:80

#VOLUMES = -v /var/log/docker:/var/log
VOLUMES= -v /var/run/docker.sock:/tmp/docker.sock:ro

#ENV = -e SOME_KEY=SOME_VALUE
INSTANCE = default
DOCKER ?= docker

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