import psycopg2

hostname = '192.168.99.101'
username = 'docker'
password = 'secret'
database = 'justpc'

def openConnection():
   return psycopg2.connect( host=hostname, user=username, password=password, dbname=database ) 

def closeConnection(connection):
    connection.close()
