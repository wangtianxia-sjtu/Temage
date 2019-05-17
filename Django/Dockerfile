# FROM ubuntu:16.04

# MAINTAINER dianaaaa

# # Install required packages and remove the apt packages cache when done.

# RUN apt-get update && \
#     apt-get upgrade -y && \ 	
#     apt-get install -y \
# 	git \
# 	python3 \
# 	python3-dev \
# 	python3-setuptools \
# 	python3-pip \
# 	nginx \
#     wget\
# 	fontconfig\
# 	libxrender1\
# 	xfonts-75dpi\
# 	xfonts-base\
# 	supervisor &&\
# 	pip3 install -U pip setuptools && \
#    rm -rf /var/lib/apt/lists/*

# # install uwsgi now because it takes a little while
# RUN pip3 install uwsgi

# # setup all the configfiles
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# COPY temage_nginx.conf /etc/nginx/sites-available/default
# COPY dockerconf/supervisor-app.conf /etc/supervisor/conf.d/

# COPY . /home/docker/code/
# RUN pip3 install -r /home/docker/code/requirements.txt

# EXPOSE 8000
# WORKDIR /home/docker/code
# RUN wget http://se.archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
# RUN dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb
# RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb
# RUN dpkg -i wkhtmltox_0.12.5-1.xenial_amd64.deb

# CMD ["supervisord", "-n"]

From dianaaaa/server-a:v6 

COPY . /home/docker/code/
# CMD ["supervisord", "-n"]