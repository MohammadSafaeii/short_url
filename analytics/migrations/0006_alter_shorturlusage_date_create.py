# Generated by Django 4.2.4 on 2023-08-09 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0005_alter_shorturlusage_date_create"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturlusage",
            name="date_create",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date used"
            ),
        ),
    ]
