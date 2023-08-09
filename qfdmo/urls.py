from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("analyse", views.analyse, name="analyse"),
    path(
        "analyse/<int:id>",
        views.analyse_acteur_reemploi,
        name="analyse_acteur_reemploi",
    ),
]
