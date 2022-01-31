# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import BaseAnketa, PeriodsAnketa

admin.site.register(BaseAnketa)
admin.site.register(PeriodsAnketa)
