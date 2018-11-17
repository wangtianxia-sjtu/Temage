from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_sex = models.BooleanField(default=0)
    def __str__(self):
        return self.user.username

class Style(models.Model):
    style_id = models.IntegerField(primary_key=True)
    style_path = models.CharField(max_length=255)
    def __str__(self):
        return self.style_id

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_path = models.CharField(max_length=255)
    product_score = models.FloatField(null=True)
    user = models.ForeignKey(Profile,to_field="user", on_delete=models.CASCADE)
    style = models.ForeignKey(Style, to_field="style_id", on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
