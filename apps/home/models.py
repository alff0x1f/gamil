# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class Colors(models.TextChoices):
    WHITE = 'WHITE', 'Белый'
    PINK = 'PINK', 'Розовый'
    GREEN = 'GREEN', 'Зеленый'
    YELLOW = 'YELLOW', 'Желтый'
    RED = 'RED', 'Красный'


class Anketa(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    color = models.CharField(max_length=10, choices=Colors.choices,
                             default=Colors.WHITE)
    file = models.FileField(upload_to='data/upload', )
    long_text = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
