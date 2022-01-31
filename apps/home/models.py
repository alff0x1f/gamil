# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.models import User
from django.db import models


class Age(models.TextChoices):
    a20_25 = "age_20_25", "20-25"
    a26_30 = "age_26_30", "26-30"
    a31_35 = "age_31_35", "31-35"
    a36_40 = "age_36_40", "36-40"
    a41_45 = "age_41_45", "41-45"
    a46_50 = "age_46_50", "46-50"


class Colors(models.TextChoices):
    WHITE = "WHITE", "Белый"
    PINK = "PINK", "Розовый"
    GREEN = "GREEN", "Зеленый"
    YELLOW = "YELLOW", "Желтый"
    RED = "RED", "Красный"


class Menarche(models.TextChoices):
    CH1 = "24-38/3-8", "24-38/3-8"
    CH2 = "24-38/>8", "24-38/>8"
    CH3 = "23 и </3-8", "23 и </3-8"
    CH4 = "23 и </>8", "23 и </>8"
    other = "другое", "другое"


class PeriodsType(models.TextChoices):
    BIG = "Обильные", "Обильные"
    NORMAL = "нормальные", "нормальные"
    SMALL = "судные", "судные"


class BaseAnketa(models.Model):
    full_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.CharField(max_length=15, choices=Age.choices)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} - {self.age}"


class PeriodsAnketa(models.Model):
    # color = models.CharField(
    #     max_length=10, choices=Colors.choices, default=Colors.WHITE
    # )
    # file = models.FileField(upload_to="data/upload",)
    # long_text = models.TextField()
    menarche = models.CharField(max_length=20, choices=Menarche.choices)
    periods_type = models.CharField(max_length=20, choices=PeriodsType.choices)
    year_break = models.IntegerField()
    periods_break_variant = models.CharField(max_length=20, choices=Menarche.choices)
    break_type = models.CharField(max_length=20, choices=PeriodsType.choices)
    blood = models.BooleanField()
    blood_year = models.IntegerField(null=True, blank=True)
    #
    # dt_created = models.DateTimeField(auto_now_add=True)
