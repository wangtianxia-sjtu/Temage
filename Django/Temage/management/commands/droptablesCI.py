#-*-coding:utf-8-*-
from django.core.management.base import BaseCommand, CommandError
import pymysql
class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            connect = pymysql.connect(
                user="root",
                password="",
                host="mysql",
                port=3306,
                charset="utf8"
            )
            cursor = connect.cursor()
            cursor.execute('drop database if exists temage')
            cursor.execute('create database temage')

        except:
            raise CommandError("The droptablesCI command has something wrong.")
        else:
            self.stdout.write('Successfully init the database')