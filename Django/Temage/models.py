from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idnumber = models.IntegerField(default=1)
    phone = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='photo')
    def __str__(self):
        return self.user.username
