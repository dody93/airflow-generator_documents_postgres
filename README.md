# Generate Bulk Documents Python

It is a python script that generate bulk documents automatically from postgres data using replace concept. It can be used to generate bulk documents like letters, cards and certificates. It read data from an excel sheet and generate multiple documents.


# Important Note
If this repository helped you to understand at least something new please give star this repository which motivates me to work further for the similar kinds for projects.

# Prerequisites
In order to run the python script, your system must have the following programs/packages installed.

Dodcker  download it https://docs.docker.com/desktop/install/windows-install/
Apache Airflow download it from https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
Python 3.8: Download it from https://www.python.org/downloads
Pandas : Run in command prompt pip install pandas
docxtpl : Run in command prompt pip install docxtpl
python-docx: Run in command prompt pip install python-docx

# Approach
First need to clone this respiratory.
Run DAG using airflow
The script reads data from postgres data, replace texts and generate documents.

 
