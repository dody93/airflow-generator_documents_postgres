from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from script.document_generator_postgress import script
from datetime import datetime,timedelta




default_args = {
    'owner' : 'Dody93'
}




with DAG(
    dag_id='dag_generate_documents_postgres',
    default_args=default_args,
    start_date=datetime(2023, 6, 13),
    schedule_interval='@hourly',
    max_active_runs=1
) as dag:


    load_file = PythonOperator(
        task_id='task_1', 
        python_callable= script

    )
     #initiate task
    start_task  = DummyOperator(
    task_id='start_task'
    )
    
    end_task    = DummyOperator(
    task_id='end_task'
    )

start_task >> load_file >> end_task
