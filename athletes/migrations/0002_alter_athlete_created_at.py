# Generated by Django 4.1.1 on 2022-10-01 17:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("athletes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="athlete",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
