from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# create a function that will be called when the user accesses the root of the website
def get_db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) # create a connection to the database
    conn.row_factory = sqlite3.Row # The line of code assigning sqlite3.Row to the row_factory of connection creates what some people call a 'dictionary cursor', - instead of tuples it starts returning 'dictionary' rows after fetchall or fetchone
    # for more information about these two lines, good conversation on stackoverflow: https://stackoverflow.com/questions/44009452/what-is-the-purpose-of-the-row-factory-method-of-an-sqlite3-connection-object found there
    return conn

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/Section')
def Section():
    return 'This is class 504'

@app.route('/Assignment')
def Assignment():
    return 'This is FLASK assignment'

@app.route('/patients')
def patients():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql:', patientListSql)
    return render_template('index.html', data=patientListSql)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)