from django.contrib.gis.db import models
from django.forms import model_to_dict

from qfdmo.models.utils import NomAsNaturalKeyModel


class ActionDirection(NomAsNaturalKeyModel):
    class Meta:
        verbose_name = "Direction de l'action"
        verbose_name_plural = "Directions de l'action"

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, unique=True, blank=False, null=False)
    order = models.IntegerField(blank=False, null=False, default=0)
    nom_affiche = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nom_affiche


class Action(NomAsNaturalKeyModel):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, unique=True, blank=False, null=False)
    nom_affiche = models.CharField(max_length=255, null=False, default="")
    description = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(blank=False, null=False, default=0)
    lvao_id = models.IntegerField(blank=True, null=True)
    directions = models.ManyToManyField(ActionDirection)
    couleur = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="yellow-tournesol",
        help_text="""Couleur du badge à choisir dans le DSFR
Couleur dispoible : blue-france, green-tilleul-verveine, green-bourgeon, green-emeraude,
green-menthe, green-archipel, blue-ecume, blue-cumulus, purple-glycine, pink-macaron,
pink-tuile, yellow-tournesol, yellow-moutarde, orange-terre-battue, brown-cafe-creme,
brown-caramel, brown-opera, beige-gris-galet""",
    )
    icon = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Icône du badge à choisir dans le <a href='https://www.systeme-de-design.gouv.fr/elements-d-interface/fondamentaux-techniques/icones' target='_blank'>DSFR</a>",  # noqa E501
    )

    def serialize(self):
        return model_to_dict(self, exclude=["directions"])