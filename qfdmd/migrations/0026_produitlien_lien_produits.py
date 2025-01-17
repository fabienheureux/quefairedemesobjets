# Generated by Django 5.1.1 on 2025-01-07 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmd", "0025_remove_lien_produits_alter_produit_nom"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProduitLien",
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
                ("poids", models.IntegerField(default=0)),
                (
                    "lien",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="qfdmd.lien"
                    ),
                ),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="qfdmd.produit"
                    ),
                ),
            ],
            options={
                "ordering": ("poids",),
                "unique_together": {("produit", "lien")},
            },
        ),
        migrations.AddField(
            model_name="lien",
            name="produits",
            field=models.ManyToManyField(
                help_text="Produits associés",
                related_name="liens",
                through="qfdmd.ProduitLien",
                to="qfdmd.produit",
            ),
        ),
    ]
