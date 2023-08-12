# Generated by Django 4.2.4 on 2023-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_shorturlusage_browser_alter_shorturlusage_device"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShortUrlUsageLastDay",
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
                ("general_count", models.IntegerField()),
                ("general_count_per_user", models.IntegerField()),
                ("device_count", models.JSONField()),
                ("device_count_per_user", models.JSONField()),
                ("browser_count", models.JSONField()),
                ("browser_count_per_user", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="ShortUrlUsageLastMonth",
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
                ("general_count", models.IntegerField()),
                ("general_count_per_user", models.IntegerField()),
                ("device_count", models.JSONField()),
                ("device_count_per_user", models.JSONField()),
                ("browser_count", models.JSONField()),
                ("browser_count_per_user", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="ShortUrlUsageLastWeek",
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
                ("general_count", models.IntegerField()),
                ("general_count_per_user", models.IntegerField()),
                ("device_count", models.JSONField()),
                ("device_count_per_user", models.JSONField()),
                ("browser_count", models.JSONField()),
                ("browser_count_per_user", models.JSONField()),
            ],
        ),
    ]