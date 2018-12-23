from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.BooleanField(default=0)
    avator = models.ImageField(upload_to='img/avator')
    def __str__(self):
        return self.user.username

class Style(models.Model):
    sid = models.IntegerField(primary_key=True)
    spath = models.CharField(max_length=255)
    def __str__(self):
        return self.style_id

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=255)
    pimag = models.ImageField(upload_to='img/pimg')
    html = models.TextField(blank=True)
    theme = models.CharField(max_length=225)
    #ppath = models.CharField(max_length=255)
    pscore = models.FloatField(null=True)
    time = models.DateTimeField(auto_now=True)
    pcreator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.pid

class Card(models.Model):
    cid = models.IntegerField(primary_key=True)
    ccreator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    prompt = models.TextField()

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pids = models.IntegerField()

    
