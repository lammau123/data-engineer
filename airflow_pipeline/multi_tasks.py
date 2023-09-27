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
    