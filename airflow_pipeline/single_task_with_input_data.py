from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import pendulum

def task_name_with_input(input_data):
    print('This is the demo of input data={data}'.format(data=input_data))
    
default_args = {
    'owner': 'OwnerName',
    #days_ago = 2 means current date - 2 days. This makes sure it schedule correctly to current day
    'start_date': pendulum.today('UTC').add(days=-2),
    #timedetla=1 daily schedule
    'schedule_interval': timedelta(days=1)
}

with DAG(
    dag_id = 'single_task_with_input',
    description = 'This is a single task dag test.',
    default_args = default_args,
    tags = ['single_task_with_input']
) as dag:
    task = PythonOperator(
        task_id = 'single_task_with_input_id',
        python_callable = task_name_with_input,
        #input value for task
        op_kwargs={'input_data': 'input value demo'}
    )

##config pipeline here
task