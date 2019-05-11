# Temage
2018 Intel Competition

## Develop

1. make sure you have installed some dependencies

   ``` bash
   cd /your/local/path/Temage
   pip install -r requirements.txt
   ```

2. modify Django configs and tornado configs

   ``` bash
   cd /your/local/path/Temage/Django/Django
   vim settings.py
   # modify configs
   # you should be careful for ALLOWED_HOSTS, DATABASES
   cd /your/local/path/Temage/tornado
   vim config.py
   # modify configs
   # you should be careful for ALLOWED_HOSTS, DATABASES
   ```

3. migrate models into database(we have diy commands to simplify the process)

   ``` bash
   cd /your/local/path/Temage/Django
   python manage.py cleanmigration # clean migration files
   python manage.py droptables # clean the db
   python manage.py makemigrations Temage # convert models to migrations
   python manage.py migrate # migrate into the database
   ```

4. start Django server and Tornado server

   ``` bash
   cd /your/local/path/Temage/Django
   python manage.py runserver 0.0.0.0:8080# start Django server
   cd /your/local/path/Temage/tornado
   python server.py
   ```

5. start ElasticSearch & Kibana

   ```bash
   cd /your/local/path/ElasticSearch # start elastic application
   ./bin/elasticsearch
   cd /your/local/path/Kibana # start kibana application
   ./bin/kibana
   ```

   

## Deploy

almost the same as the develop, but pay attention to some settings

1. Django

   ```python
   # settings.py
   # SECURITY WARNING: don't run with debug turned on in production!
   DEBUG = False
   
   ALLOWED_HOSTS = [] #set specific hosts
   ```

2. tornado

   ```python
   # config.py
   # ...
   
   settings = {
   	...
       "debug": False
   }
   ```
## CI/CD Script
``` bash
# start from pure python environment
cd your/local/path/Temage/Django
pip install django
pip install pymysql
pip install django-cors-headers
pip install django_polymorphic
pip install pyjwt
pip install Pillow
python manage.py cleanmigration && python manage.py droptables && python manage.py makemigrations Temage && python manage.py migrate Temage && python manage.py test
```
if there is anything wrong, please contact administrator.

### cluster deploy

Temage uses kubernetes + Istio  to deploy the service, the whole configs about the cluster  are in the cluster_config.