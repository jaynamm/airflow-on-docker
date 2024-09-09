import textwrap
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    "spark_test",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
    },
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2024, 9, 1),
    catchup=False,
    tags=["example"],
) as dag:
    spark_test = SparkSubmitOperator(
        task_id = "spakr_test",
        conn_id = "spark_default",
        application="/Users/jhnam/workspace/airflow-on-docker/dags/scripts/test.py",
    )
    
    spark_test