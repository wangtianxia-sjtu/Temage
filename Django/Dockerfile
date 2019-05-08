FROM ubuntu:16.04

MAINTAINER dianaaaa

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \ 	
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
    wget\
	fontconfig\
	libxrender1\
	xfonts-75dpi\
	xfonts-base\
	supervisor &&\
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY temage_nginx.conf /etc/nginx/sites-available/default
# RUN ln -s ~/home/docker/code/temage_nginx.conf /etc/nginx/sites-enabled/
COPY dockerconf/supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY . /home/docker/code/
RUN pip3 install -r /home/docker/code/requirements.txt
# RUN chmod +x /home/docker/code/entrypoint.sh
# RUN python3 /home/docker/code/Django/manage.py collectstatic


# add (the rest of) our code
# COPY . /home/docker/code/

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# RUN django-admin.py startproject website /home/docker/code/app/

EXPOSE 8000
WORKDIR /home/docker/code
RUN wget http://se.archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
RUN dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb
RUN dpkg -i wkhtmltox_0.12.5-1.xenial_amd64.deb
# RUN mv /usr/local/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf.backup
# RUN mv /usr/local/bin/wkhtmltoimage /usr/local/bin/wkhtmltoimage.backup
# RUN rm /usr/local/bin/wkhtmltopdf.backup
# RUN rm /usr/local/bin/wkhtmltoimage.backup
# ENTRYPOINT ["sh", "/home/docker/code/entrypoint.sh"]
CMD ["supervisord", "-n"]

# RUN cd /home/docker/code/Django
# RUN uwsgi --http :8001 --module Django.wsgi