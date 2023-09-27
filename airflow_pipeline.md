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

#### Transfer Data Between Tasks in Pipeline

