from django.core.management.base import BaseCommand

from signalwire.rest import Client as signalwire_client
client = signalwire_client('51447a44-b545-48f3-b3fb-b47ab9800c75',
                           'PTa364413f2bc16652c59adf1b119593ddd531423ae3a560be'
                           signalwire_space_url = 'goodmorning.signalwire.com')

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("test")
        print("Hi")

