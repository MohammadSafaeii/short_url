# Generated by Django 4.2.4 on 2023-08-09 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0006_alter_shorturlusage_date_create"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturlusage",
            name="date_create",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 8, 8, 9, 17, 36, 6668, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date used",
            ),
        ),
    ]