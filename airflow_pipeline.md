# How to Create Airflow Pipeline
A pipeline includes a series tasks, these tasks are configured to execute in a specified order to achieve a specific data processing or ETL (Extract, Transform, Load) goal. the output of one finished task can be an input of next tasks. Airflow provides a way to define, schedule, and monitor these pipelines using Python code.
#### Single Task Pipeline
* Create a python file and copy the below code or get file file from here [code](/airflow_pipeline/single_task.py) and copy it to ~\airflow\dags folder
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
import pendulum

# this is python function presents a task
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
    default_args = default_args
) as dag:
    task = PythonOperator(
        task_id = 'single_task_id',
        python_callable = task_name
    )

##config pipeline here
task
```
* Dag list shows on the Airflow page
![Dags](/assets/images/single_task_dag.png)
* Task Graph shows on the Airflow page
![Dags](/assets/images/single_task.png)
#### Task Input Data Pipeline
* Create a python file and copy the below code or get file file from here [code](/airflow_pipeline/single_task_with_input_data.py) and copy it to ~\airflow\dags folder
```python
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
```
* Task Log shows on the Airflow page
![Dags](/assets/images/single_task_with_input.png)
#### Multiple Tasks Pipeline
* Create a python file and copy the below code or get file file from here [code](/airflow_pipeline/multi_tasks.py) and copy it to ~\airflow\dags folder
```python
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

def multi_task1():
    print('This is multi task1 running.')
    
def multi_task2():
    print('This is multi task1 running.')
    
def multi_task3():
    print('This is multi task1 running.')
    
def multi_task4():
    print('This is multi task1 running.')
    
default_args = {
    'owner': 'OwnerName',
    #days_ago = 1 means current date - 1 day. This makes sure it schedule correctly to current day
    'start_date': pendulum.today('UTC').add(days=-1),
    'schedule_interval': '@daily'
}

with DAG(
    dag_id = 'multi_tasks_dag_id',
    description = 'This is multi tasks demo',
    default_args = default_args,
    tags = ['multi_tasks']
) as dag:
    task1 = PythonOperator(
        task_id = 'multi_task1_id',
        python_callable = multi_task1
    )
    task2 = PythonOperator(
        task_id = 'multi_task2_id',
        python_callable = multi_task2
    )
    task3 = PythonOperator(
        task_id = 'multi_task3_id',
        python_callable = multi_task3
    )
    task4 = PythonOperator(
        task_id = 'multi_task4_id',
        python_callable = multi_task4
    )
    
#Configure pipeline 
# task1 executes first then task2 and task3 execute simultaneously then task4
task1 >> [task2, task3] >> task4
```
* Task Graph shows on the Airflow page
![Dags](/assets/images/multi_tasks.png)
#### Transfer Data Between Tasks in Pipeline
* Create a python file and copy the below code or get file file from here [code](/airflow_pipeline/multi_tasks_with_input_data.py) and copy it to ~\airflow\dags folder
```python

```
* Tasks logs shows on the Airflow page
![Dags](/assets/images/multi_tasks_log1.png)
![Dags](/assets/images/multi_tasks_log2.png)


