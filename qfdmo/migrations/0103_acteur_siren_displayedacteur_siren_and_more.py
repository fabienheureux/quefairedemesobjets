# Generated by Django 5.1.1 on 2024-12-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0102_alter_action_couleur_alter_groupeaction_couleur_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="acteur",
            name="siren",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name="displayedacteur",
            name="siren",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name="displayedacteurtemp",
            name="siren",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name="revisionacteur",
            name="siren",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
