# Generated by Django 5.0.4 on 2024-07-10 09:54

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0076_displayedpropositionservicetempsouscategorie_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="acteur",
            name="exclusivite_de_reprisereparation",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="acteur",
            name="public_accueilli",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Particuliers et professionnels",
                        "Particuliers et professionnels",
                    ),
                    ("Professionnels", "Professionnels"),
                    ("Particuliers", "Particuliers"),
                    ("Aucun", "Aucun"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="acteur",
            name="reprise",
            field=models.CharField(
                blank=True,
                choices=[("1 pour 0", "1 pour 0"), ("1 pour 1", "1 pour 1")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="acteur",
            name="uniquement_sur_rdv",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="displayedacteur",
            name="exclusivite_de_reprisereparation",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="displayedacteur",
            name="public_accueilli",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Particuliers et professionnels",
                        "Particuliers et professionnels",
                    ),
                    ("Professionnels", "Professionnels"),
                    ("Particuliers", "Particuliers"),
                    ("Aucun", "Aucun"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="displayedacteur",
            name="reprise",
            field=models.CharField(
                blank=True,
                choices=[("1 pour 0", "1 pour 0"), ("1 pour 1", "1 pour 1")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="displayedacteur",
            name="uniquement_sur_rdv",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="displayedacteurtemp",
            name="exclusivite_de_reprisereparation",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="displayedacteurtemp",
            name="public_accueilli",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Particuliers et professionnels",
                        "Particuliers et professionnels",
                    ),
                    ("Professionnels", "Professionnels"),
                    ("Particuliers", "Particuliers"),
                    ("Aucun", "Aucun"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="displayedacteurtemp",
            name="reprise",
            field=models.CharField(
                blank=True,
                choices=[("1 pour 0", "1 pour 0"), ("1 pour 1", "1 pour 1")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="displayedacteurtemp",
            name="uniquement_sur_rdv",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="revisionacteur",
            name="exclusivite_de_reprisereparation",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AddField(
            model_name="revisionacteur",
            name="public_accueilli",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "Particuliers et professionnels",
                        "Particuliers et professionnels",
                    ),
                    ("Professionnels", "Professionnels"),
                    ("Particuliers", "Particuliers"),
                    ("Aucun", "Aucun"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="revisionacteur",
            name="reprise",
            field=models.CharField(
                blank=True,
                choices=[("1 pour 0", "1 pour 0"), ("1 pour 1", "1 pour 1")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="revisionacteur",
            name="uniquement_sur_rdv",
            field=models.BooleanField(db_default=False, default=False),
        ),
        migrations.AlterField(
            model_name="acteur",
            name="cree_le",
            field=models.DateTimeField(
                auto_now_add=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="acteur",
            name="modifie_le",
            field=models.DateTimeField(
                auto_now=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="acteur",
            name="statut",
            field=models.CharField(
                choices=[
                    ("ACTIF", "actif"),
                    ("INACTIF", "inactif"),
                    ("SUPPRIME", "supprimé"),
                ],
                db_default="ACTIF",
                default="ACTIF",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteur",
            name="cree_le",
            field=models.DateTimeField(
                auto_now_add=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteur",
            name="modifie_le",
            field=models.DateTimeField(
                auto_now=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteur",
            name="statut",
            field=models.CharField(
                choices=[
                    ("ACTIF", "actif"),
                    ("INACTIF", "inactif"),
                    ("SUPPRIME", "supprimé"),
                ],
                db_default="ACTIF",
                default="ACTIF",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteurtemp",
            name="cree_le",
            field=models.DateTimeField(
                auto_now_add=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteurtemp",
            name="modifie_le",
            field=models.DateTimeField(
                auto_now=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="displayedacteurtemp",
            name="statut",
            field=models.CharField(
                choices=[
                    ("ACTIF", "actif"),
                    ("INACTIF", "inactif"),
                    ("SUPPRIME", "supprimé"),
                ],
                db_default="ACTIF",
                default="ACTIF",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="revisionacteur",
            name="cree_le",
            field=models.DateTimeField(
                auto_now_add=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="revisionacteur",
            name="modifie_le",
            field=models.DateTimeField(
                auto_now=True, db_default=django.db.models.functions.datetime.Now()
            ),
        ),
        migrations.AlterField(
            model_name="revisionacteur",
            name="statut",
            field=models.CharField(
                choices=[
                    ("ACTIF", "actif"),
                    ("INACTIF", "inactif"),
                    ("SUPPRIME", "supprimé"),
                ],
                db_default="ACTIF",
                default="ACTIF",
                max_length=255,
            ),
        ),
    ]