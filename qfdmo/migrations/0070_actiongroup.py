# Generated by Django 5.0.4 on 2024-05-03 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0069_assign_ess"),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupeAction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=255, unique=True)),
                ("afficher", models.BooleanField(default=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("order", models.IntegerField(default=0)),
                (
                    "couleur",
                    models.CharField(
                        blank=True,
                        default="yellow-tournesol",
                        help_text="Couleur du badge à choisir dans le DSFR\nCouleur dispoible : blue-france, green-tilleul-verveine, green-bourgeon, green-emeraude,\ngreen-menthe, green-archipel, blue-ecume, blue-cumulus, purple-glycine, pink-macaron,\npink-tuile, yellow-tournesol, yellow-moutarde, orange-terre-battue, brown-cafe-creme,\nbrown-caramel, brown-opera, beige-gris-galet",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        help_text="Icône du badge à choisir dans le <a href='https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icones' rel='noopener' target='_blank'>DSFR</a>",
                        max_length=255,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Groupe d'actions",
                "verbose_name_plural": "Groupes d'actions",
            },
        ),
        migrations.AddField(
            model_name="action",
            name="libelle_groupe",
            field=models.CharField(
                default="",
                help_text="Libellé de l'action dans le groupe",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="groupe_action",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actions",
                to="qfdmo.GroupeAction",
            ),
        ),
    ]