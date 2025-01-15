# Generated by Django 5.1.1 on 2024-11-22 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmd", "0012_suggestion"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="suggestion",
            name="id",
        ),
        migrations.AlterField(
            model_name="suggestion",
            name="produit",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="qfdmd.produit",
            ),
        ),
    ]
