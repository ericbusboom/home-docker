
#NS = wordpress
#VERSION = careerpath

#REPO = wp-dc-vol
#NAME = wp-dc-vol
INSTANCE = default
DOCKER ?= docker

# NOTE! Docker-compose gets the project name from the directory the compose file is in, 
# or the -p option, or the COMPOSE_PROJECT_NAME environmental variable. 
PROJECT_NAME=wpmultisite

VOLUMES= \
-v $(PROJECT_NAME)_database:/var/lib/mysql \
-v $(PROJECT_NAME)_code:/code \
-v $(PROJECT_NAME)_html:/var/www/html

.PHONY: build push shell run start stop restart reload rm rmf release enablemulti

#build:
#	$(DOCKER) build -t $(NS)/$(REPO):$(VERSION) .

#push:
#	$(DOCKER) push $(NS)/$(REPO):$(VERSION)

shell:
	$(DOCKER) run --rm -i -t $(PORTS) $(VOLUMES) $(ENV) ubuntu /bin/bash

# Turn on wordpress multisite
enablemulti:
	$(DOCKER) run --rm -i -t $(PORTS) $(VOLUMES) $(ENV) wordpress:careerpath  /usr/local/bin/enable-multisite.sh
    

	
#busybox cp -r /src/updraftplus.zip /var/www/html/wp-content/plugins


#attach:
#	$(DOCKER) exec  -ti $(NAME) /bin/bash

#run:
# 	$(DOCKER) run --rm --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

#logs:
#	$(DOCKER) logs -f $(NAME) 

#start:
#	$(DOCKER) run -d --name $(NAME) $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(REPO):$(VERSION)

#stop:
#	$(DOCKER) stop $(NAME)
	
#restart: stop start
#
#reload: build rmf start
#
#rmf:
#	$(DOCKER) rm -f $(NAME)

#rm:
#	$(DOCKER) rm $(NAME)

#release: build
#	make push -e VERSION=$(VERSION)

default: build