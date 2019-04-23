from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

#run to get the sql:
#python manage.py sqlmigrate main 0001
