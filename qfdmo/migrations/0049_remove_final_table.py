# Generated by Django 4.2.9 on 2024-03-22 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0048_alter_correctionacteur_final_acteur_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            "DROP MATERIALIZED VIEW qfdmo_finalpropositionservice_sous_categories;",
        ),
        migrations.RunSQL(
            "DROP MATERIALIZED VIEW qfdmo_finalpropositionservice;",
        ),
        migrations.RunSQL(
            "DROP MATERIALIZED VIEW qfdmo_finalacteur;",
        ),
    ]