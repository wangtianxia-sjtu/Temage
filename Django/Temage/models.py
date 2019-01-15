from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Theme(models.Model):
    tname = models.CharField(max_length=50,default="tname")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extension")
    sex = models.BooleanField(default=0)
    phone = models.CharField(max_length=15, null=False)
    avator = models.ImageField(upload_to='img/avator')
    intrest = models.ManyToManyField(Theme)
    def __str__(self):
        return self.user.username

class Style(models.Model):
    sname = models.CharField(max_length=50, default="name")
    spath = models.CharField(max_length=255, default="path")
    def __str__(self):
        return self.sname

class Product(models.Model):
    ptitle = models.CharField(max_length=255, default="title")
    pimag = models.ImageField(upload_to='img/pimg')
    html = models.TextField(blank=True)
    theme = models.ManyToManyField(Theme)
    #ppath = models.CharField(max_length=255)
    pscore = models.FloatField(null=True)
    time = models.DateTimeField(auto_now=True)
    pcreator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.ptitle

class Card(models.Model):
    curl = models.CharField(max_length=255, default="localhost")
    ccreator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cproduct = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    ctitle = models.CharField(max_length=50)
    cprompt = models.TextField()
    def __str__(self):
        return self.ctitle

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    colname = models.CharField(max_length=50,default="name")
    cards = models.ManyToManyField(Card)
    def __str__(self):
        return self.colname


    
