from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import pendulum

def task_name():
    print('This is single task demo.')
    
default_args = {
    'owner': 'OwnerName',
    #days_ago = 2 means current date - 2 days. This makes sure it schedule correctly to current day
    'start_date': pendulum.today('UTC').add(days=-2),
    #timedetla=1 daily schedule
    'schedule_interval': timedelta(days=1)
}

with DAG(
    dag_id = 'single_task',
    description = 'This is a single task dag test.',
    default_args = default_args,
    tags = ['single_task']
) as dag:
    task = PythonOperator(
        task_id = 'single_task_id',
        python_callable = task_name
    )

##config pipeline here
task