# Generated by Django 5.1.1 on 2024-11-06 08:27

from django.db import migrations


def assign_non_reparacteur_cma(apps, schema_editor):
    Source = apps.get_model("qfdmo", "Source")
    Acteur = apps.get_model("qfdmo", "Acteur")
    RevisionActeur = apps.get_model("qfdmo", "RevisionActeur")
    source_cma_historique, _ = Source.objects.get_or_create(
        code="Longue Vie Aux Objets"
    )
    acteurs_cma_non_reparacteur = Acteur.objects.filter(
        source__code="CMA - Chambre des métiers et de l'artisanat"
    ).exclude(labels__code="reparacteur")
    acteurs_cma_non_reparacteur.update(source=source_cma_historique)
    RevisionActeur.objects.filter(
        identifiant_unique__in=acteurs_cma_non_reparacteur.values_list(
            "identifiant_unique", flat=True
        )
    ).update(source=source_cma_historique)


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0098_alter_action_couleur_alter_groupeaction_couleur"),
    ]

    operations = [
        migrations.RunPython(assign_non_reparacteur_cma, migrations.RunPython.noop)
    ]
