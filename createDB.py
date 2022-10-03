import sqlite3
connect = sqlite3.connect('./patients.db')
db = connect.cursor()




# // commit () --> This method commits the current transaction. If you don't call this method, 
# anything you did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            sex CHAR(25) NOT NULL,
            race CHAR(25) NOT NULL,
            age INT(25) NOT NULL,
            gender CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes, this is annoying but necessary


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('12345', 'John', 'Smith', '01/01/2000', 'female', 'white', 22, 'woman')")

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('23456', 'Jane', 'Doe', '02/02/2001', 'female', 'black', 21, 'woman')")

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('34567', 'Mary', 'Smith', '03/03/2002', 'female', 'black', 20, 'woman')")

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('45678', 'Bob', 'Smith', '04/04/2003', 'male', 'hispanic', 19, 'man')")

db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('56789', 'Jane', 'Doe', '05/05/2004', 'female', 18, 'asian', 'woman')")

dummyPerson6 = """ INSERT INTO patient_table(mrn, firstname, lastname, dob, sex, race, age, gender) values('32323', 'John321', 'Smith123', '01/01/2000', 'male', 'black', 22, 'man') """
db.execute(dummyPerson6)

connect.commit()


# close the connection
connect.close()