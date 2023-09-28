# Import necessary modules from Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import modules for date and time handling
from datetime import timedelta
import pendulum

# Define a Python function that represents the task's functionality
def task_name_with_input(input_data):
    print('This is the demo of input data={data}'.format(data=input_data))

# Define default arguments for the DAG
default_args = {
    'owner': 'OwnerName',  # Specify the owner or creator of the DAG
    'start_date': pendulum.today('UTC').add(days=-2),  # Define the start date for task scheduling
    'schedule_interval': timedelta(days=1)  # Define the schedule interval (in this case, daily)
}

# Create a new DAG instance with a unique ID, description, and tags
with DAG(
    dag_id='single_task_with_input',  # Unique identifier for the DAG
    description='This is a single task DAG test.',  # Description of the DAG
    default_args=default_args,  # Assign the default arguments defined earlier
    tags=['single_task_with_input']  # Assign tags to categorize the DAG
) as dag:
    # Define a PythonOperator task within the DAG
    task = PythonOperator(
        task_id='single_task_with_input_id',  # Unique identifier for the task
        python_callable=task_name_with_input,  # Specify the Python function to execute for this task
        # Define input data for the task using op_kwargs
        op_kwargs={'input_data': 'input value demo'}
    )

## Define task to be executed in pipeline
task
