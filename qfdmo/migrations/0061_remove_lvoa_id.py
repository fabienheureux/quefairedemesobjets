# Generated by Django 4.2.9 on 2024-04-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0060_source_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="acteurservice",
            name="lvao_id",
        ),
        migrations.RemoveField(
            model_name="acteurtype",
            name="lvao_id",
        ),
        migrations.RemoveField(
            model_name="action",
            name="lvao_id",
        ),
        migrations.RemoveField(
            model_name="souscategorieobjet",
            name="lvao_id",
        ),
    ]