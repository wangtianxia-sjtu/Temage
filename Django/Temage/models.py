from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extension")
    sex = models.BooleanField(default=0)
    phone = models.CharField(max_length=15, null=False)
    avator = models.ImageField(upload_to='img/avator')
    interest = models.ManyToManyField(Theme)
    def __str__(self):
        return self.user.username

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    def __str__(self):
        return self.id

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    imag = models.ImageField(upload_to='img/pimg')
    html = models.TextField(blank=True)
    theme = models.ManyToManyField(Theme)
    #path = models.CharField(max_length=255)
    score = models.FloatField(null=True)
    time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.id

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    prompt = models.TextField()
    def __str__(self):
        return self.id

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card)
    def __str__(self):
        return self.id


    
