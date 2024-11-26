import pandas as pd
import pytest
from sources.tasks.business_logic.propose_acteur_services import propose_acteur_services


@pytest.fixture
def acteurservice_id_by_code():
    return {"service_de_reparation": 10, "structure_de_collecte": 20}


class TestCreateActeurServices:
    # TODO : refacto avec parametize
    def test_create_acteur_services_empty(self, acteurservice_id_by_code):

        df_result = propose_acteur_services(
            df_actors=pd.DataFrame(
                {
                    "identifiant_unique": [1, 2],
                    "point_dapport_de_service_reparation": [False, False],
                    "point_dapport_pour_reemploi": [False, False],
                    "point_de_reparation": [False, False],
                    "point_de_collecte_ou_de_reprise_des_dechets": [False, False],
                }
            ),
            acteurservice_id_by_code=acteurservice_id_by_code,
        )

        assert df_result.empty
        assert df_result.columns.tolist() == [
            "acteur_id",
            "acteurservice_id",
        ]

    def test_create_acteur_services_full(self, acteurservice_id_by_code):

        df_result = propose_acteur_services(
            df_actors=pd.DataFrame(
                {
                    "identifiant_unique": [1, 2],
                    "point_dapport_de_service_reparation": [True, True],
                    "point_dapport_pour_reemploi": [True, True],
                    "point_de_reparation": [True, True],
                    "point_de_collecte_ou_de_reprise_des_dechets": [True, True],
                }
            ),
            acteurservice_id_by_code=acteurservice_id_by_code,
        )

        assert df_result.columns.tolist() == [
            "acteur_id",
            "acteurservice_id",
        ]
        assert sorted(
            df_result.loc[df_result["acteur_id"] == 1, "acteurservice_id"].tolist()
        ) == [
            10,
            20,
        ]
        assert sorted(
            df_result.loc[df_result["acteur_id"] == 2, "acteurservice_id"].tolist()
        ) == [
            10,
            20,
        ]

    def test_create_acteur_services_only_one(self, acteurservice_id_by_code):

        df_result = propose_acteur_services(
            df_actors=pd.DataFrame(
                {
                    "identifiant_unique": [1, 2],
                    "point_dapport_de_service_reparation": [True, False],
                    "point_dapport_pour_reemploi": [False, True],
                    "point_de_reparation": [False, False],
                    "point_de_collecte_ou_de_reprise_des_dechets": [False, False],
                }
            ),
            acteurservice_id_by_code=acteurservice_id_by_code,
        )

        assert df_result.columns.tolist() == [
            "acteur_id",
            "acteurservice_id",
        ]
        assert sorted(
            df_result.loc[df_result["acteur_id"] == 1, "acteurservice_id"].tolist()
        ) == [10]
        assert sorted(
            df_result.loc[df_result["acteur_id"] == 2, "acteurservice_id"].tolist()
        ) == [20]