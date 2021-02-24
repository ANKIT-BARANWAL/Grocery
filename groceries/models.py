from django.conf import settings
from django.db import models
from django.utils import timezone


class Grocery(models.Model):
    item_id=models.IntegerField()
    title = models.CharField(max_length=850)
    price = models.FloatField()
    description=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return self.title