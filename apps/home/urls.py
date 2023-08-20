# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path

from apps.home import views
from apps.home.views import (
    AnketaSuccessView,
    AnketaView,
    ArteryEmbolizationView,
    DoctorView,
    NewAnketaView,
    PeriodsView,
)

urlpatterns = [
    # The home page
    path("", NewAnketaView.as_view(), name="home"),
    path("anketa/<int:pk>/", AnketaView.as_view(), name="anketa"),
    path(
        "anketa/<int:pk>/periods/",
        PeriodsView.as_view(),
        name="periods",
    ),
    path(
        "anketa/<int:pk>/doctor/",
        DoctorView.as_view(),
        name="doctor",
    ),
    path(
        "anketa/<int:pk>/artery_embolization/",
        ArteryEmbolizationView.as_view(),
        name="artery_embolization",
    ),
    path(
        "anketa/<int:pk>/success/",
        AnketaSuccessView.as_view(),
        name="anketa_success",
    ),
    # Matches any html file
    re_path(r"^.*\.*", views.pages, name="pages"),
]
