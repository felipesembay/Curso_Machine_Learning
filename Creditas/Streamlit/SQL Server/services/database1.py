import pyodbc 
import mysql.connector
import pandas as pd
import sqlalchemy

server = '172.17.0.3,1433' 
database = 'Creditas' 
username = 'sa' 
password = 'abc123456' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()


#cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:creditas-teste.database.windows.net,1433;Database=Creditas_curso;Uid=felipe_sembay;Pwd={abc123456!@};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
#cursor = cnxn.cursor()