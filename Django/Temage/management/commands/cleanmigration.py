from django.core.management.base import BaseCommand, CommandError
import os
class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            path = "./Temage/migrations/"
            misc = os.listdir(path)
            for element in misc:
                if os.path.isfile(path+element):
                    os.remove(path+element)
                    self.stdout.write('delete'+element)    
            f = open(path+"__init__.py","w")
            f.close()

        except:
            raise CommandError("The seed command has something wrong.")
        else:
            self.stdout.write('Successfully clean migrations')