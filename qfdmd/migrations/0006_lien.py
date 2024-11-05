# Generated by Django 5.1.1 on 2024-11-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmd", "0005_rename_libelle_produit_nom_produit_bdd_produit_code_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lien",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "titre_du_lien",
                    models.CharField(
                        blank=True, unique=True, help_text="Titre du lien"
                    ),
                ),
                ("url", models.URLField(blank=True, help_text="URL", max_length=300)),
                ("description", models.TextField(blank=True, help_text="Description")),
                (
                    "produits",
                    models.ManyToManyField(
                        help_text="Produits associés",
                        related_name="liens",
                        to="qfdmd.produit",
                    ),
                ),
            ],
        ),
    ]
