# Generated by Django 4.2.6 on 2023-10-29 08:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("qfdmo", "0027_alter_correctionacteur_final_acteur_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            """
                    DROP MATERIALIZED VIEW IF EXISTS qfdmo_finalpropositionservice_sous_categories;
                    DROP MATERIALIZED VIEW IF EXISTS qfdmo_finalpropositionservice;

                    CREATE MATERIALIZED VIEW qfdmo_finalpropositionservice AS
                        WITH ra AS
                        (SELECT ra.identifiant_unique
                        FROM qfdmo_revisionacteur AS ra
                        LEFT OUTER JOIN qfdmo_revisionpropositionservice AS rps ON rps.revision_acteur_id = ra.identifiant_unique
                        GROUP BY ra.identifiant_unique
                        HAVING count(rps.id) >0),
                            a AS
                        (SELECT a.identifiant_unique
                        FROM qfdmo_acteur AS a
                        WHERE a.identifiant_unique NOT IN
                            (SELECT *
                                FROM ra)),
                            ps AS
                        (SELECT id AS original_id,
                                acteur_service_id,
                                action_id,
                                acteur_id
                        FROM qfdmo_propositionservice
                        WHERE acteur_id IN
                            (SELECT *
                                FROM a) ),
                            rps AS
                        (SELECT id AS original_id,
                                acteur_service_id,
                                action_id,
                                revision_acteur_id AS acteur_id
                        FROM qfdmo_revisionpropositionservice
                        WHERE revision_acteur_id IN
                            (SELECT *
                                FROM ra) ),
                            ps_rps AS
                        (SELECT *, FALSE AS is_revision
                        FROM ps
                        UNION SELECT *, TRUE AS is_revision
                        FROM rps)

                        SELECT row_number() OVER (ORDER BY acteur_id) AS id, *
                        FROM ps_rps;
                    CREATE UNIQUE INDEX ON qfdmo_finalpropositionservice(id);

                    CREATE MATERIALIZED VIEW qfdmo_finalpropositionservice_sous_categories AS
                        WITH sous_cat_a AS
                        (SELECT fps.id AS finalpropositionservice_id,
                                psc.souscategorieobjet_id
                        FROM qfdmo_propositionservice_sous_categories AS psc
                        INNER JOIN qfdmo_finalpropositionservice AS fps ON psc.propositionservice_id = fps.original_id
                        AND is_revision IS FALSE),
                            sous_cat_ra AS
                        (SELECT fps.id AS finalpropositionservice_id,
                                psc.souscategorieobjet_id
                        FROM qfdmo_revisionpropositionservice_sous_categories AS psc
                        INNER JOIN qfdmo_finalpropositionservice AS fps ON psc.revisionpropositionservice_id = fps.original_id
                        AND is_revision IS TRUE) ,
                            sous_cat AS
                        (SELECT *
                        FROM sous_cat_a
                        UNION SELECT *
                        FROM sous_cat_ra)
                        SELECT row_number() OVER (
                                                ORDER BY finalpropositionservice_id,
                                                        souscategorieobjet_id) AS id,
                                                *
                        FROM sous_cat;
                    CREATE UNIQUE INDEX ON qfdmo_finalpropositionservice_sous_categories(id);
            """,
            """
                    DROP MATERIALIZED VIEW IF EXISTS qfdmo_finalpropositionservice_sous_categories;
                    DROP MATERIALIZED VIEW IF EXISTS qfdmo_finalpropositionservice;

                    CREATE MATERIALIZED VIEW qfdmo_finalpropositionservice AS
                        SELECT row_number() OVER (ORDER BY a.identifiant_unique) as id,
                            a.identifiant_unique AS acteur_id,
                            COALESCE(rps.action_id, ps.action_id) AS action_id,
                            COALESCE(rps.acteur_service_id, ps.acteur_service_id) AS acteur_service_id
                        FROM qfdmo_acteur AS a
                        LEFT OUTER JOIN qfdmo_revisionacteur AS ra ON a.identifiant_unique = ra.identifiant_unique
                        LEFT OUTER JOIN qfdmo_propositionservice AS ps ON ps.acteur_id = a.identifiant_unique AND ra.identifiant_unique IS NULL
                        LEFT OUTER JOIN qfdmo_revisionpropositionservice AS rps ON rps.revision_acteur_id = a.identifiant_unique;
                    CREATE UNIQUE INDEX ON qfdmo_finalpropositionservice(id);

                    CREATE MATERIALIZED VIEW qfdmo_finalpropositionservice_sous_categories AS
                        SELECT row_number() OVER (ORDER BY a.identifiant_unique) as id,
                        	fps.id AS finalpropositionservice_id,
                            COALESCE(rps_sc.souscategorieobjet_id, ps_sc.souscategorieobjet_id) AS souscategorieobjet_id
                        FROM qfdmo_acteur AS a
                        LEFT OUTER JOIN qfdmo_revisionacteur AS ra ON a.identifiant_unique = ra.identifiant_unique
                        LEFT OUTER JOIN qfdmo_propositionservice AS ps ON ps.acteur_id = a.identifiant_unique AND ra.identifiant_unique IS NULL
                        LEFT OUTER JOIN qfdmo_revisionpropositionservice AS rps ON rps.revision_acteur_id = a.identifiant_unique
                        LEFT OUTER JOIN qfdmo_finalpropositionservice AS fps ON fps.acteur_id = a.identifiant_unique AND fps.action_id = COALESCE(rps.action_id, ps.action_id) and COALESCE(rps.acteur_service_id, ps.acteur_service_id) = fps.acteur_service_id
                        LEFT OUTER JOIN qfdmo_propositionservice_sous_categories AS ps_sc ON ps_sc.propositionservice_id = ps.id AND ps.id IS NOT NULL
                        LEFT OUTER JOIN qfdmo_revisionpropositionservice_sous_categories AS rps_sc ON rps_sc.revisionpropositionservice_id = rps.id AND rps.id IS NOT NULL
                        WHERE (rps_sc.revisionpropositionservice_id IS NOT NULL OR ps_sc.propositionservice_id IS NOT NULL);
                    CREATE UNIQUE INDEX ON qfdmo_finalpropositionservice_sous_categories(id);
            """,
        ),
    ]
