FROM postgres:latest

RUN apt-get -y update && \
apt-get -y upgrade && \
apt-get install -y build-essential python3 python3-pip
RUN pip3 install psycopg2-binary