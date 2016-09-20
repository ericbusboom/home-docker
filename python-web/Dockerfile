FROM jfloff/alpine-python:2.7

RUN pip install --upgrade pip
RUN pip install flask

# for a flask server
WORKDIR /var/docker-fs
EXPOSE 80 
CMD flask run -h 0.0.0.0 -p 80

