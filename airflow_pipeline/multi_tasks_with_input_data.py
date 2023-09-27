import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

def multi_task1(input_data):
    input_data = input_data + 'task1: start'
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
    print('This is multi task2 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data
    
def multi_task4(input_data):
    input_data = input_data + ' task4: start'
    print('This is multi task4 running with input data = {data}.'.format(data=input_data))
    input_data = input_data + '-done.'
    return input_data
    
default_args = {
    'owner': 'OwnerName',
    #days_ago = 1 means current date - 1 day. This makes sure it schedule correctly to current day
    'start_date': pendulum.today('UTC').add(days=-1),
    'schedule_interval': '@daily'
}

with DAG(
    dag_id = 'multi_tasks_with_input_dag_id',
    description = 'This is multi tasks demo',
    default_args = default_args,
    tags = ['multi_tasks']
) as dag:
    task1 = PythonOperator(
        task_id = 'multi_task1_id',
        python_callable = multi_task1,
        #input value for task
        op_kwargs={'input_data': ''}
    )
    task2 = PythonOperator(
        task_id = 'multi_task2_id',
        python_callable = multi_task2,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task1_id')}}"}
    )
    task3 = PythonOperator(
        task_id = 'multi_task3_id',
        python_callable = multi_task3,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task1_id')}}"}
    )
    task4 = PythonOperator(
        task_id = 'multi_task4_id',
        python_callable = multi_task4,
        op_kwargs={'input_data': "{{ti.xcom_pull('multi_task2_id')}} - {{ti.xcom_pull('multi_task3_id')}}"}
    )
    
#Configure pipeline 
# task1 executes first then task2 and task3 execute simultaneously then task4
task1 >> [task2, task3] >> task4
    