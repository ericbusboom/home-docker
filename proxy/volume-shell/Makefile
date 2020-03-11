
NS = busboom.org
VERSION = latest

REPO = nginx-proxy-volume-container
NAME = nginx-proxy-volume-container
INSTANCE = default
DOCKER ?= docker

# NOTE! Docker-compose gets the project name from the directory the compose file is in, 
# or the -p option, or the COMPOSE_PROJECT_NAME environmental variable. 
PROJECT_NAME=coreweb

VOLUMES= \
-v $(PROJECT_NAME)_etc-nginx-conf:/volumes/etc/nginx/conf.d \
-v $(PROJECT_NAME)_etc-nginx-vhost:/volumes/etc/nginx/vhost.d \
-v $(PROJECT_NAME)_usr-share-nginx-html:/volumes/usr/share/nginx/html \
-v $(PROJECT_NAME)_etc-nginx-certs:/volumes/etc/nginx/certs \
-v $(PROJECT_NAME)_etc-dockergen-templates:/volumes/etc/docker-gen/templates \
-v $(PROJECT_NAME)_var-lib-postgresql:/volumes/var/lib/postgresql \
-v $(PROJECT_NAME)_var-backups-postgresql:/volumes/var/backups/postgresql \
-v $(PROJECT_NAME)_home-redmine-data:/volumes/home/redmine/data 

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

backup:
	$(DOCKER) run --rm  $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION) tar -czf - /volumes  | tar -xzvf -

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