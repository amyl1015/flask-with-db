import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('./patients.db')
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# save the data to a dataframe
df = pd.DataFrame(patientListSql)
print(df)
print(df.columns)

# # rename the columns
# df.columns = ['mrn', 'firstname', 'lastname', 'dob']
# df