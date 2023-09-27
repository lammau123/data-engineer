# How to Install Apache Airflow on Window 11

## 1. Prerequisuites
Before installing Apache Airflow on Windows 11, you need to set up the Windows Subsystem for Linux (WSL2). Follow the instructions provided *[here](https://github.com/lammau123/data-engineer/blob/main/wsl.md)* to install WSL2 on your system.
## 2. Requirements:
To complete this tutorial, you will need the following:

* Python 3.8 or higher
* Windows 11 or higher
* Windows Subsystem for Linux (WSL2)

## 3. Install Python 
Verify your Python version by running the following command in your WSL terminal:
```code
python3 --version
```
If you don't have Python 3 or need a specific version, you can install it with:
```code
sudo apt-get install python3.10
```
## 4. Install pip
```code
sudo apt install python3-pip
```
## 5. Install python3-virtualenv
Install the virtual environment package with:
```code
sudo apt install python3-virtualenv
```
## 6. Create a Virtual Environment
Navigate to the folder where you want to create a new virtual environment and run:
```code
virtualenv airflow_environment
```
## 7. Activate a Virtual Environment
```code
source airflow_environment/bin/activate
```
## 8. Create Airflow Home Directory
Create a directory to store Airflow files:
```code
mkdir airflow
```
## 9. Install Apache Airflow
Install Apache Airflow using pip3:
```code
pip3 install apache-airflow
```

## 10. Set AIRFLOW_HOME Path
Edit your profile file using the vi editor:
```code
vi ~/.profile
```
Add the following line to set the AIRFLOW_HOME path, replacing [username] with your username:
```code
AIRFLOW_HOME=/home/[username]/airflow
```
After making this change, log out of your WSL session and log in again for the changes to take effect.
## 11. Initialize the Airflow Database
```code
airflow db init
```
## 12. Create an Airflow Admin User
Create an admin user for Airflow with the following command, replacing [username], [password], [name], [lastname], and [youremail@email.com] with your preferred values:
```code
airflow users create --username [username] --password [password] --firstname [name] --lastname [lastname] --role Admin --email youremail@email.com
```
## 13. Start the Airflow Scheduler
Run the Airflow scheduler:
```code
airflow scheduler
```
## 14. Start the Airflow Web Server
Run the Airflow web server with an assigned port number:
```code
airflow webserver --port <port number>
```
## 15. Access the Airflow Web Interface
Open your web browser and navigate to *http://localhost:[port]. Use the credentials you created in the previous step to log in to the Airflow web interface.

Your Apache Airflow installation on Windows 11 is now complete, and you can start using it for your data engineering tasks.

