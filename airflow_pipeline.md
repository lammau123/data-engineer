# How to Create Airflow Pipeline
An Apache Airflow pipeline consists of a series of tasks configured to execute in a specific order, allowing you to achieve various data processing or ETL (Extract, Transform, Load) goals. Each task can take the output of the previous one as input, creating a directed acyclic graph (DAG). Airflow provides a Python-based framework to define, schedule, and monitor these pipelines. This guide demonstrates how to create different types of pipelines.

## 1. Single Task Pipeline
#### Step 1: Create a Python file and place it in the ~/airflow/dags folder. You can copy the code below as a starting point or get source code from [here](/airflow_pipeline/single_task.py)
```python
# Import necessary modules from Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import modules for date and time handling
from datetime import timedelta
import pendulum

# Define a Python function that represents the task's functionality
def task_name():
    print('This is a single task demo.')

# Define default arguments for the DAG
default_args = {
    'owner': 'OwnerName',  # Specify the owner or creator of the DAG
    'start_date': pendulum.today('UTC').add(days=-2),  # Define the start date for task scheduling
    'schedule_interval': timedelta(days=1)  # Define the schedule interval (in this case, daily)
}

# Create a new DAG instance with a unique ID and description
with DAG(
    dag_id='single_task',  # Unique identifier for the DAG
    description='This is a single task DAG test.',  # Description of the DAG
    default_args=default_args  # Assign the default arguments defined earlier
) as dag:
    # Define a PythonOperator task within the DAG
    task = PythonOperator(
        task_id='single_task_id',  # Unique identifier for the task
        python_callable=task_name  # Specify the Python function to execute for this task
    )

# Configuration for the DAG is defined above, and the 'task' is the final step that represents the task itself.
task
```
#### Step 2: Your DAG will now be visible on the Airflow web interface. You can view it in the DAGs list.
![Dags](/assets/images/single_task_dag.png)
#### Step 3: To visualize the task execution, navigate to the Task Graph on the Airflow web page.
![Dags](/assets/images/single_task.png)

## 2. Task Input Data Pipeline
#### Step 1: Create another Python file in the ~/airflow/dags folder, or you can copy the code below to ~/airflow/dags folder or get source code from [here](/airflow_pipeline/single_task_with_input_data.py)
```python
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
```
#### Step 2: The task execution and logs can be viewed on the Airflow web interface.
![Dags](/assets/images/single_task_with_input.png)

## 3. Multiple Tasks Pipeline
#### Step 1: Create another Python file in the ~/airflow/dags folder, or you can copy the code below to ~/airflow/dags folder or get source code from
[here](/airflow_pipeline/multi_tasks.py)
```python
# Import necessary modules from Airflow
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define Python functions for multiple tasks
def multi_task1():
    print('This is multi task1 running.')

def multi_task2():
    print('This is multi task2 running.')

def multi_task3():
    print('This is multi task3 running.')

def multi_task4():
    print('This is multi task4 running.')

# Define default arguments for the DAG
default_args = {
    'owner': 'OwnerName',  # Specify the owner or creator of the DAG
    'start_date': pendulum.today('UTC').add(days=-1),  # Define the start date for task scheduling
    'schedule_interval': '@daily'  # Define the schedule interval (in this case, daily)
}

# Create a new DAG instance with a unique ID, description, and tags
with DAG(
    dag_id='multi_tasks_dag_id',  # Unique identifier for the DAG
    description='This is multi tasks demo',  # Description of the DAG
    default_args=default_args,  # Assign the default arguments defined earlier
    tags=['multi_tasks']  # Assign tags to categorize the DAG
) as dag:
    # Define PythonOperator tasks within the DAG
    task1 = PythonOperator(
        task_id='multi_task1_id',  # Unique identifier for the task
        python_callable=multi_task1  # Specify the Python function to execute for this task
    )
    task2 = PythonOperator(
        task_id='multi_task2_id',
        python_callable=multi_task2
    )
    task3 = PythonOperator(
        task_id='multi_task3_id',
        python_callable=multi_task3
    )
    task4 = PythonOperator(
        task_id='multi_task4_id',
        python_callable=multi_task4
    )

# Configure the pipeline
# task1 executes first, followed by task2 and task3 executing simultaneously, and then task4
task1 >> [task2, task3] >> task4
```
#### Step 2: The Task Graph on the Airflow web page visualizes the task relationships in the DAG
![Dags](/assets/images/multi_tasks.png)

## 4. Data Transfer Between Tasks in Pipeline
#### Step 1: Create another Python file in the ~/airflow/dags folder, or you can copy the code below to ~/airflow/dags folder or get source code from here [code](/airflow_pipeline/multi_tasks_with_input_data.py)
```python
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
        # Pass the output from 'multi_task1_id' as 'input_data' using XCom
        # XCom allows sharing data between tasks within the same DAG
        # The "{{ }}" syntax is used for templating, and it references the output of the 'multi_task1_id' task
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
```
#### Step 2: The Task Logs on the Airflow web page display the execution of tasks with input data.
![Dags](/assets/images/multi_tasks_log1.png)
![Dags](/assets/images/multi_tasks_log2.png)

This guide provides a comprehensive overview of creating various types of pipelines in Apache Airflow, helping you orchestrate complex data workflows efficiently.
