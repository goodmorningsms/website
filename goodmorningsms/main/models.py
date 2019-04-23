from django.db import models
from datetime import datetime

# Create your models here.


class Numbers(models.Model):
        phone = models.IntegerField(default=1)
        date_added = models.DateTimeField("date published", default=datetime.now())


        #def __str__(self):
            #return self.phone

