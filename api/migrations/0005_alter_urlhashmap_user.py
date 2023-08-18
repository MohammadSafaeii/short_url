# Generated by Django 4.2.4 on 2023-08-12 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0004_urlhashmap_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlhashmap",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="url_hashmaps",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]