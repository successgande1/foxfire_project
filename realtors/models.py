from django.db import models

from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='photos/%Y/%m/%d')
    description = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.name

