from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField()
    email= models.EmailField()
    phone = models.CharField(max_length=10)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
