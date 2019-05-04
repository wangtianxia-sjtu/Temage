FROM dianaaaa/ubuntu16.04-python3.6:v2

MAINTAINER dianaaaa

# Install required packages and remove the apt packages cache when done.

# RUN apt-get update && \
#     apt-get upgrade -y && \ 	
#     apt-get install -y \
# 	git \
# 	python3 \
# 	python3-dev \
# 	python3-setuptools \
# 	python3-pip && \
# 	pip3 install -U pip setuptools && \
#    rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
# RUN pip3 install uwsgi

# setup all the configfiles
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# COPY temage_nginx.conf /etc/nginx/sites-available/default
# RUN ln -s ~/home/docker/code/temage_nginx.conf /etc/nginx/sites-enabled/
# COPY dockerconf/supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY . /home/docker/code/
# RUN pip3 install -r /home/docker/code/requirements.txt
# RUN chmod +x /home/docker/code/entrypoint.sh
# RUN python3 /home/docker/code/Django/manage.py collectstatic


# add (the rest of) our code
# COPY . /home/docker/code/

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
# RUN django-admin.py startproject website /home/docker/code/app/

EXPOSE 8000
WORKDIR /home/docker/code/
# ENTRYPOINT ["python3", "server.py"]
CMD ["python", "server.py"]

# RUN cd /home/docker/code/Django
# RUN uwsgi --http :8001 --module Django.wsgi
