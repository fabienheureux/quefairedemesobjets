# Generated by Django 5.0.4 on 2024-04-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0067_categorieobjet_code_and_dagrun"),
    ]

    operations = [
        migrations.AddField(
            model_name="labelqualite",
            name="type_enseigne",
            field=models.BooleanField(
                default=False,
                help_text="Ce label est affiché comme un type d'enseigne, ex : ESS",
            ),
        ),
    ]