from django.contrib import admin
from .models import Profile
from .models import User
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

