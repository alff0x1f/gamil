# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import ArteryEmbolizationModel, BaseAnketa, DoctorAnketa, PeriodsAnketa

admin.site.register(BaseAnketa)
admin.site.register(PeriodsAnketa)
admin.site.register(DoctorAnketa)
admin.site.register(ArteryEmbolizationModel)
