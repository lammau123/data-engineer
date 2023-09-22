# How to install Linux on Windows with WSL

Window Subsystem for Linux (WSL) lets developer run linux on window OS at the same time. 

#### Prerequisites
You must be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11 to use the commands below. If you are on earlier versions please see the manual install page.

#### Install WSL
Open window commandline and run the below code
* List all support distribution
```code
wsl --list --online
```
* Install wsl
```code
wsl --install -d Ubuntu
```
* Once Ubuntu installed, update and then upgrade it
```code
sudo apt-get update
sudo apt-get upgrade
```
