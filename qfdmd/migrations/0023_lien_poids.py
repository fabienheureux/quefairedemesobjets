# Generated by Django 5.1.1 on 2025-01-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmd", "0022_synonyme_comment_les_eviter_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="lien",
            name="poids",
            field=models.IntegerField(default=0),
        ),
    ]
