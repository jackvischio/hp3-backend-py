import mysql.connector
from os import environ as env

par = env["SQL_PARAMS"]
params = par.split('#')

connection = mysql.connector.connect(
    user=params[0], 
    password=params[1],
    host=params[2],
    database=params[3]
)

#"hockeypistadb#xdcer9-Kflaom-fako1a#www.db4free.net#hockeypista"