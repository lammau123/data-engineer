## How to Run Postgres from Binary Package on Window 11

This guide provides step-by-step instructions on setting up PostgreSQL using a binary package without the need for installation. PostgreSQL is a powerful open-source database system, and this approach allows you to quickly get it up and running.
#### 1. Introduction
A database is a structured collection of data managed by a Database Management System (DBMS). A DBMS is responsible for storing, retrieving, modifying, and deleting data efficiently. There are various types of databases, including:

* Relational databases
* NoSQL databases
* Object-oriented databases
* Hierarchical databases
* Network databases
  
PostgreSQL, often referred to as Postgres, stands out as an Object-Relational Database (ORD). It combines the best of both worlds, supporting relational and object-oriented features. This means that PostgreSQL allows the direct representation of objects, classes, and inheritance in database schemas and the query language.
#### 2. Prerequisites
Before you begin, ensure that your system meets these minimal hardware requirements:

* 1 GHz processor
* 2 GB of RAM
* 512 MB of available hard disk space
  
Please note that these requirements are the bare minimum for basic functionality. For optimal performance or when dealing with larger databases, it's advisable to allocate more resources.

#### 3. Downloading the Binary Package
Start by downloading the PostgreSQL binary package for Windows 11:

Download Link: https://www.enterprisedb.com/download-postgresql-binaries
#### 4. Installing PostgreSQL
Follow these steps to set up PostgreSQL:

* Extract the downloaded package to your desired location (e.g., C:\databases\postgres).
* Create a dedicated folder for storing database files (e.g., C:\databases\data).
* Initialize a database cluster using the following command:
```code
C:\databases\postgres\bin> initdb -D C:\databases\data
```

#### 5. Starting database server
Once you've successfully run initdb, the database cluster configuration is created in the C:\databases\data folder. Now, proceed to start the PostgreSQL server:
```code
C:\databases\postgres\bin>pg_ctl -D "C:\databases\data" logfile start
```

#### 6. Testing the Installation
To verify that PostgreSQL is up and running, perform the following tests:
* List all pre-created databases on the server:
```code
C:\databases\postgres\bin>psql -l
```

* Connect to the PostgreSQL database with appropriate parameters:
```code
C:\databases\postgres\bin>psql -h localhost -p 5432 -d postgres -U lamma
```
** -h: hostname
** -p: port
** -d: databasename
** -U: ownername

* Create a new database, e.g., "testdb":
```code
postgres=# CREATE DATABASE testdb
```

* Switch to the newly created database:
```code
postgres=# \c testdb
```

* Create a schema:
```code
testdb=# CREATE SCHEMA schema1;
```

* Create a table within the schema:
```code
testdb=# CREATE TABLE schema1.my_table (
    name text,
    date date
);
```

* Inserting data into the table:
```code
testdb=# INSERT INTO schema1.my_table(name, date) VALUES('name1', '12/01/2023');
testdb=# INSERT INTO schema1.my_table(name, date) VALUES('name1', '12/01/2023');
```

* Query the inserted data
```code
testdb=# SELECT * FROM schema1.my_table;
```

Congratulations! You've successfully set up and tested PostgreSQL from a binary package on Windows 11.

