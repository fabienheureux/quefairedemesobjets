# Generated by Django 5.1.1 on 2024-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("qfdmo", "0097_displayedacteur_uuid_displayedacteurtemp_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="couleur",
            field=models.CharField(
                blank=True,
                default="yellow-tournesol",
                help_text="Couleur du badge à choisir dans le DSFR\nCouleurs disponibles : blue-france, green-tilleul-verveine, green-bourgeon,\ngreen-emeraude, green-menthe, green-archipel, blue-ecume, blue-cumulus, purple-glycine,\npink-macaron, pink-tuile, yellow-tournesol, yellow-moutarde, orange-terre-battue,\nbrown-cafe-creme, brown-caramel, brown-opera, beige-gris-galet, pink-tuile-850,\ngreen-menthe-850,green-bourgeon-850, yellow-moutarde-850, blue-ecume-850,\ngreen-menthe-sun-373,blue-cumulus-sun-368, orange-terre-battue-main-645,\nbrown-cafe-creme-main-782, purple-glycine-main-494, green-menthe-main-548,\nbrown-caramel-sun-425-hover\n",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="groupeaction",
            name="couleur",
            field=models.CharField(
                blank=True,
                default="yellow-tournesol",
                help_text="Couleur du badge à choisir dans le DSFR\nCouleurs disponibles : blue-france, green-tilleul-verveine, green-bourgeon,\ngreen-emeraude, green-menthe, green-archipel, blue-ecume, blue-cumulus, purple-glycine,\npink-macaron, pink-tuile, yellow-tournesol, yellow-moutarde, orange-terre-battue,\nbrown-cafe-creme, brown-caramel, brown-opera, beige-gris-galet, pink-tuile-850,\ngreen-menthe-850,green-bourgeon-850, yellow-moutarde-850, blue-ecume-850,\ngreen-menthe-sun-373,blue-cumulus-sun-368, orange-terre-battue-main-645,\nbrown-cafe-creme-main-782, purple-glycine-main-494, green-menthe-main-548,\nbrown-caramel-sun-425-hover\n",
                max_length=255,
                null=True,
            ),
        ),
    ]