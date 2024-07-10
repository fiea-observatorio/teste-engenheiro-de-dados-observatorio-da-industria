import pendulum

from airflow.decorators import dag
from airflow.providers.papermill.operators.papermill import PapermillOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["observatorio@sistemafiea.com.br"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": pendulum.duration(minutes=5),
}

@dag(
    default_args=default_args,
    description="DAG para pesquisa industrial anual de empresas",
    schedule=None,
    start_date=pendulum.datetime(2024, 3, 22, tz="America/Sao_Paulo"),
    catchup=False,
)

def pesquisa_industrial_anual_empresas():
    import os

    PapermillOperator(
        task_id="workspace",
        input_nb=os.path.join(
            os.getcwd(),
            "dags",
            "{{ dag.dag_id }}",
            "notebooks",
            "workspace.ipynb",
        ),
        output_nb="/opt/airflow/dags/resultado/{{ dag.dag_id }}_{{ task.task_id }}_{{ ds }}.ipynb",
    )

pesquisa_industrial_anual_empresas()
