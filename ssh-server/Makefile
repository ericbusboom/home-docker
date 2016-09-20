INSTANCE = default
DOCKER ?= docker

NS = gaff
VERSION = latest

REPO = alpine-sshd

DOCKER ?= docker

PORTS =  -p 80 -p 2222:22

NAME=docker-fs

VOLUMES= -v /share/docker/docker-fs:/var/docker-fs
ENV = -e AUTHORIZED_KEY="`cat ~/.ssh/id_rsa.pub`" -e VIRTUAL_HOST=dockerfs.busboom.org

.PHONY: build push shell run start stop restart reload rm rmf release

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