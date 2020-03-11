#!/bin/sh



cp /tmp/nginx.tmpl /etc/docker-gen/templates/nginx.tmpl

exec /usr/local/bin/docker-gen ""$@""