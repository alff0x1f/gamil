# Generated by Django 3.2.19 on 2023-06-22 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="arteryembolizationmodel",
            options={
                "verbose_name": "Cелективная эмболизация маточных артерий",
                "verbose_name_plural": "Cелективные эмболизации маточных артерий",
            },
        ),
        migrations.AlterModelOptions(
            name="baseanketa",
            options={
                "verbose_name": "Базовая анкета",
                "verbose_name_plural": "Базовые анкеты",
            },
        ),
        migrations.AlterModelOptions(
            name="doctoranketa",
            options={
                "verbose_name": "Анкета врача",
                "verbose_name_plural": "Анкеты врачей",
            },
        ),
        migrations.AlterModelOptions(
            name="periodsanketa",
            options={
                "verbose_name": "Менструальная функция",
                "verbose_name_plural": "Менструальная функция",
            },
        ),
    ]