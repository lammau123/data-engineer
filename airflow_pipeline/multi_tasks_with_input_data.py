# Import necessary modules from Airflow
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define Python functions for multiple tasks, each receiving input_data as an argument
def multi_task1(input_data):
    input_data = input_data + ' task1: start'
    print('This is multi task1 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data

def multi_task2(input_data):
    input_data = input_data + ' task2: start'
    print('This is multi task2 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data

def multi_task3(input_data):
    input_data = input_data + ' task3: start'
        print('This is multi task3 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data

def multi_task4(input_data):
    input_data = input_data + ' task4: start'
    print('This is multi task4 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data

# Define default arguments for the DAG
default_args = {
    'owner': 'OwnerName',  # Specify the owner or creator of the DAG
    'start_date': pendulum.today('UTC').add(days=-1),  # Define the start date for task scheduling
    'schedule_interval': '@daily'  # Define the schedule interval (in this case, daily)
}

# Create a new DAG instance with a unique ID, description, and tags
with DAG(
    dag_id='multi_tasks_with_input_dag_id',  # Unique identifier for the DAG
    description='This is multi tasks demo',  # Description of the DAG
    default_args=default_args,  # Assign the default arguments defined earlier
    tags=['multi_tasks']  # Assign tags to categorize the DAG
) as dag:
    # Define PythonOperator tasks within the DAG
    task1 = PythonOperator(
        task_id='multi_task1_id',  # Unique identifier for the task
        python_callable=multi_task1,  # Specify the Python function to execute for this task
        op_kwargs={'input_data': ''}  # Provide an initial input_data value for task1
    )
    task2 = PythonOperator(
        task_id='multi_task2_id',
        python_callable=multi_task2,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task1_id')}}"}
    )
    task3 = PythonOperator(
        task_id='multi_task3_id',
        python_callable=multi_task3,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task1_id')}}"}
    )
    task4 = PythonOperator(
        task_id='multi_task4_id',
        python_callable=multi_task4,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task2_id')}} - {{ti.xcom_pull('multi_task3_id')}}"}
    )

# Configure the pipeline
# task1 executes first, followed by task2 and task3 executing simultaneously, and then task4
task1 >> [task2, task3] >> task4
