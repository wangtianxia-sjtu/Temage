#-*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

# Create your models here.
class CommonThemes(PolymorphicModel):
    id = models.AutoField(primary_key=True)


class Style(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    css = models.FileField(upload_to='css')

    def __str__(self):
        return (self.id)


class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    owner = models.ManyToManyField(CommonThemes, related_name='theme')
    styles = models.ManyToManyField(Style, related_name='themes')

    def __str__(self):
        return (self.id)


class Profile(CommonThemes):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    # sex = models.BooleanField(default=0)
    # phone = models.CharField(max_length=15, null=False)
    avator = models.ImageField(upload_to='img/avator')
    vector = models.TextField(blank=True)

    def __str__(self):
        return (self.user.id)


class Product(CommonThemes):
    title = models.CharField(max_length=255)
    image_src = models.ImageField(upload_to='img/pimg')
    html = models.TextField(blank=True)
    #path = models.CharField(max_length=255)
    vector = models.TextField(blank=True)
    score = models.FloatField(null=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING, related_name='products')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=0)
    width = models.IntegerField()
    html_file = models.FileField(upload_to='html')
    pdf_file = models.FileField(upload_to='pdf')

    class Meta:
        ordering = ['-update_time']

    def __str__(self):
        return str(self.id)


class Card(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cards')
    # url = models.CharField(max_length=255)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=50)
    prompt = models.TextField()
    head = models.CharField(max_length=255)
    foot_text = models.CharField(max_length = 255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return str(self.id)


class Collection(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='collection')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(Card, related_name='collections')
    prompt = models.TextField()
    url = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return str(self.id)

class Cache(models.Model):
    imgs_urls = models.TextField(blank=True)
    text = models.TextField(blank=True)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='cache')
    match_list = models.TextField(blank=True)