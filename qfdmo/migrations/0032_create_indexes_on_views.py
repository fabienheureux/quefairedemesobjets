# Generated by Django 4.2.6 on 2023-11-07 18:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("qfdmo", "0031_create_finalpropositionservice_id_index"),
    ]

    operations = [
        migrations.RunSQL(
            """
                DROP INDEX location_idx;
                CREATE INDEX qfdmo_finalacteur_location_idx ON qfdmo_finalacteur USING SPGIST (location);
                CREATE INDEX qfdmo_finalacteur_acteur_type_id_idx ON qfdmo_finalacteur(acteur_type_id);
                CREATE INDEX qfdmo_finalacteur_source_id_idx ON qfdmo_finalacteur(acteur_type_id);
            """,
            """
                DROP INDEX qfdmo_finalacteur_location_idx;
                CREATE INDEX location_idx ON qfdmo_finalacteur USING SPGIST (location);
                DROP INDEX qfdmo_finalacteur_acteur_type_id_idx;
                DROP INDEX qfdmo_finalacteur_source_id_idx;
            """,
        ),
        migrations.RunSQL(
            """
                CREATE INDEX qfdmo_finalpropositionservice_acteur_service_id_idx ON qfdmo_finalpropositionservice(acteur_service_id);
                CREATE INDEX qfdmo_finalpropositionservice_action_id_idx ON qfdmo_finalpropositionservice(action_id);
                CREATE INDEX qfdmo_finalpropositionservice_acteur_id_idx ON qfdmo_finalpropositionservice(acteur_id);
            """,
            """
                DROP INDEX qfdmo_finalpropositionservice_acteur_service_id_idx;
                DROP INDEX qfdmo_finalpropositionservice_action_id_idx;
                DROP INDEX qfdmo_finalpropositionservice_acteur_id_idx;
            """,
        ),
        migrations.RunSQL(
            """
                DROP INDEX finalpropositionservice_id_idx;
                CREATE INDEX qfdmo_fps_sc_finalpropositionservice_id_idx ON qfdmo_finalpropositionservice_sous_categories(finalpropositionservice_id);
                CREATE INDEX qfdmo_fps_sc_souscategorieobjet_id_idx ON qfdmo_finalpropositionservice_sous_categories(souscategorieobjet_id);
            """,
            """
                DROP INDEX qfdmo_fps_sc_finalpropositionservice_id_idx;
                DROP INDEX qfdmo_fps_sc_souscategorieobjet_id_idx;
                CREATE INDEX finalpropositionservice_id_idx ON qfdmo_finalpropositionservice_sous_categories(finalpropositionservice_id);
            """,
        ),
    ]