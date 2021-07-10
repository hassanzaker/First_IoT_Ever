# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Club(models.Model):
    title = models.CharField(max_length=200,
                             blank=False,
                             null=False,
                             unique=True, verbose_name='title')
    price = models.FloatField(blank=False, verbose_name='price')
