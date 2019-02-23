#-*-coding:utf-8-*-
from django.core.management.base import BaseCommand, CommandError
from Temage.models import User
from Temage.models import Profile
from Temage.models import Product
from Temage.models import Card
from Temage.models import Style
from Temage.models import Collection
from Temage.models import Theme
class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            # do something to init the db
            Style.objects.all().delete()
            Theme.objects.all().delete()
            Profile.objects.all().delete()
            User.objects.all().delete()
            Product.objects.all().delete()
            Card.objects.all().delete()
            Collection.objects.all().delete()
            self.stdout.write('hello world')
        except:
            raise CommandError("The seed command has something wrong.")
        else:
            self.stdout.write('Successfully init the database')