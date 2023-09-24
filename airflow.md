# How to Install Apache Airflow on Window 11

#### Prerequisuites
Apache Airflow runs on linux os so you need to install linux on window first. How to install Window Subsystem for Linux *[here](https://github.com/lammau123/data-engineer/blob/main/wsl.md)*.
#### Requirements:
You need Python 3.8 or higher, Windows 10 or higher, and the Windows Subsystem for Linux (WSL2) to follow this tutorial.
#### Install Python 
Check python version
```code
python3 --version
```
if not version 3, install python version 3
```code
sudo apt-get install python3.6
```
#### Install pip
```code
sudo apt install python3-pip
```
#### install python3-virtualenv
```code
sudo apt install python3-virtualenv
```
#### Before creating virtual environment you can check your current working directory.
```code
pwd
```
#### Create Virtual Environment in your current working directory
Change to a folder where you want to create a new virtual environment for python then run
```code
virtualenv airflow_environment
```
#### Active the created environment
```code
source airflow_environment/bin/activate
```
#### Create Airflow home
Where airflow will be stored
```code
mkdir airflow_home
```
#### Install Airflow
```code
pip3 install apache-airflow
```

#### Set airflow_home path to system PATH
```code
vi ~/.profile
```
add AIRFLOW_HOME=/home/[username]/airflow_home to that file and logout and login again
#### Init airflow db
```code
airflow db init
```
#### Create airflow admin user
```code
airflow users create --username [username] --password [password] --firstname [name] --lastname [lastname] --role Admin --email youremail@email.com
```
#### Run airflow schedule
```code
airflow scheduler
```
#### Run airflow webserver
```code
airflow webserver --port <port number>
```
#### Checking airflow
Open browser and input http://localhost:[port] . Use user/pass in step "Create airflow admin user" to login.

