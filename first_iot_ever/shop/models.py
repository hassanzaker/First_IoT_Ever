from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200,
                             blank=False,
                             null=False,
                             unique=True, verbose_name='title')
    price = models.FloatField(blank=False)
    count = models.IntegerField(blank=False, null=False)
    tempereture = models.FloatField(default=20.0, blank=False)

class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    slot = models.IntegerField(blank=False, null=False)