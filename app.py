# ADGSTUDIOS 2021

import random, string
from flask import Flask, session
import pyodbc


# My custom sqlserver class / module which you can find @ pip install sqlserver


# This is modded version to work for Heroku drivers change conn with your connection strings

class sqlserver():
    def __init__(self):
        pass

    def ExecuteQuery(self, Query):
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOURSQLSERVERNAME,YOURPORTNUMBER;DATABASE=YOURDBNAME;UID=YOURUSERNAME;PWD=YOURPASSWORD')
            cursor = conn.cursor()
            cursor.execute(Query)
            cursor.commit()
            print("Query Executed")
        except Exception as e:
            print(e)

    def fields(self, cur):
        results = {}
        column = 0
        for d in cur.description:
            results[d[0]] = column
            column = column + 1

        return results

    def GetRecordsOfColumn(self, SelectQuery, ColumnName):
        try:
            conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOURSQLSERVERNAME,YOURPORTNUMBER;DATABASE=YOURDBNAME;UID=YOURUSERNAME;PWD=YOURPASSWORD')
            cursor = conn.cursor()
            cursor.execute(SelectQuery)
            field_map = self.fields(cursor)
            values = []
            for row in cursor:
                values.append(row[field_map[ColumnName]])
            return values
        except Exception as e:
            print(e)

# Flask Website Engine 

app = Flask(__name__)

# Configuration for cookies

### Our Secrets
app.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
app.config['SESSION_TYPE'] = 'filesystem'   


### Functions

def TestConnection():
    bValid = False
    db = sqlserver()
    data = db.GetRecordsOfColumn('EXEC sp_helpdb','name')
    if data is None:
            bValid = False
    else:
            bValid = True
    return bValid

# We work with our website here
@app.route('/')
def index():
#Clears cookies 
    session.clear()	
    for key in list(session.keys()):
     session.pop(key)
   
    if TestConnection() == True:
         return '<h1>Database Connected Successfully :-) </h1><p>Congratulations you got your Flask/Heroku Application talking to SQL Server, Happy Hacking.</p>'
    else:
         return '<h1>Database Failed to Connect :-(</h1><p>Please look into the terminal for the error log if testing Localhost, else please check the Build Logs in Heroku or your connection string</p>'

##### if running under localhost enviroment testing grounds.
if __name__ == '__main__':    
    app.config['SESSION_TYPE'] = 'filesystem'   
    app.debug = True
    app.run(host = 'localhost', port = 8000,debug = False)



# Author : Ashlin Darius Govindasamy
