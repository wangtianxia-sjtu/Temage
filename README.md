# Temage
2018 Intel Competition

## Develop

1. make sure you have installed some dependencies

   ```shell
   cd /your/local/path/Temage
   pip install -r requirements.txt
   ```

2. modify Django configs and tornado configs

   ```shell
   cd /your/local/path/Temage/Django/Django
   vim settings.py
   # modify configs
   # you should be careful for ALLOWED_HOSTS, DATABASES
   cd /your/local/path/Temage/tornado
   vim config.py
   # modify configs
   # you should be careful for ALLOWED_HOSTS, DATABASES
   ```

3. migrate models into database

   ```shell
   cd /your/local/path/Temage/Django
   python manage.py makemigrations Temage # convert models to migrations
   python manage.py migrate Temage # migrate
   ```

4. start Django server and Tornado server

   ```shell
   cd /your/local/path/Temage/Django
   python manage.py runserver 0.0.0.0:8080# start Django server
   cd /your/local/path/Temage/tornado
   python server.py
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

if there has anything wrong, please contact with administrator.