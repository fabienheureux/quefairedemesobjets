# Generated by Django 4.2.5 on 2023-10-04 15:07

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qfdmo", "0015_finalacteur_finalpropositionservice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="action",
            name="couleur",
            field=models.CharField(
                blank=True, default="yellow-tournesol", max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="icon",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="souscategorieobjet",
            name="categorie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="qfdmo.categorieobjet"
            ),
        ),
    ]