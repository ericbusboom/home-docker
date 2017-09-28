# A Python / Flask server that runs an application in the /var/docker-fs
# directory, which is mounted on NFS when this container is run on nas 1
FROM jfloff/alpine-python:2.7

RUN pip install --upgrade pip
RUN pip install flask

# for a flask server
WORKDIR /var/docker-fs
EXPOSE 80 
CMD flask run -h 0.0.0.0 -p 80

