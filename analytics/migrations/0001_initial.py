# Generated by Django 4.2.4 on 2023-08-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortUrlUsage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shorturl", models.CharField(max_length=10)),
                ("csrf_token", models.CharField(max_length=200)),
                ("device", models.CharField(max_length=400)),
                (
                    "date_create",
                    models.DateTimeField(auto_now_add=True, verbose_name="date used"),
                ),
            ],
        ),
    ]
