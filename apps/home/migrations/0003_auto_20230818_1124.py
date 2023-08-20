# Generated by Django 3.2.19 on 2023-08-18 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0002_auto_20230622_1522"),
    ]

    operations = [
        migrations.AddField(
            model_name="arteryembolizationmodel",
            name="base_anketa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.baseanketa",
            ),
        ),
        migrations.AddField(
            model_name="baseanketa",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="doctoranketa",
            name="base_anketa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.baseanketa",
            ),
        ),
        migrations.AddField(
            model_name="periodsanketa",
            name="base_anketa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.baseanketa",
            ),
        ),
    ]
