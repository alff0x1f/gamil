# Generated by Django 3.2.6 on 2022-01-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseAnketa",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                (
                    "age",
                    models.CharField(
                        choices=[
                            ("age_20_25", "20-25"),
                            ("age_26_30", "26-30"),
                            ("age_31_35", "31-35"),
                            ("age_36_40", "36-40"),
                            ("age_41_45", "41-45"),
                            ("age_46_50", "46-50"),
                        ],
                        max_length=15,
                    ),
                ),
                ("height", models.IntegerField()),
                ("weight", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="PeriodsAnketa",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "menarche",
                    models.CharField(
                        choices=[
                            ("24-38/3-8", "24-38/3-8"),
                            ("24-38/>8", "24-38/>8"),
                            ("23 и </3-8", "23 и </3-8"),
                            ("23 и </>8", "23 и </>8"),
                            ("другое", "другое"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "periods_type",
                    models.CharField(
                        choices=[
                            ("Обильные", "Обильные"),
                            ("нормальные", "нормальные"),
                            ("судные", "судные"),
                        ],
                        max_length=20,
                    ),
                ),
                ("year_break", models.IntegerField()),
                (
                    "periods_break_variant",
                    models.CharField(
                        choices=[
                            ("24-38/3-8", "24-38/3-8"),
                            ("24-38/>8", "24-38/>8"),
                            ("23 и </3-8", "23 и </3-8"),
                            ("23 и </>8", "23 и </>8"),
                            ("другое", "другое"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "break_type",
                    models.CharField(
                        choices=[
                            ("Обильные", "Обильные"),
                            ("нормальные", "нормальные"),
                            ("судные", "судные"),
                        ],
                        max_length=20,
                    ),
                ),
                ("blood", models.BooleanField()),
                ("blood_year", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
