from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

# Create your models here.
class CommonThemes(PolymorphicModel):
    pass

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    owner = models.ManyToManyField(CommonThemes, related_name='theme')

class Profile(CommonThemes):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    # sex = models.BooleanField(default=0)
    # phone = models.CharField(max_length=15, null=False)
    avator = models.ImageField(upload_to='img/avator')
    # interest = models.ManyToManyField(Theme)
    def __str__(self):
        return self.user.username

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    def __str__(self):
        return self.id

class Product(CommonThemes):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    imagesrc = models.ImageField(upload_to='img/pimg')
    html = models.TextField(blank=True)
    # theme = models.ManyToManyField(Theme)
    #path = models.CharField(max_length=255)
    vector = models.TextField(blank=True)
    score = models.FloatField(null=True)
    time = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING, related_name='products')
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    isfinished = models.BooleanField(default=0)
    def __str__(self):
        return self.id
    class Meta:
        ordering = ['-updateTime']

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cards')
    # url = models.CharField(max_length=255)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=50)
    prompt = models.TextField()
    head = models.CharField(max_length=255)
    foottext = models.CharField(max_length = 255)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id
    class Meta:
        ordering = ['-createTime']

class Collection(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='collections')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card)
    prompt = models.TextField()
    url = models.CharField(max_length=255)
    createTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id
    class Meta:
        ordering = ['-createTime']


    
