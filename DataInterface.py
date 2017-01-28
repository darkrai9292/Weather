import json
import sqlite3

##DATES IN THE FORMAT 'DD-MM-YY'
##WINDSPEED UNITS 'm/s'
##TEMPURATURE UNITS 'celsius'
##BEARING UNITS 'degrees'

conn = sqlite3.connect('weather.db')
db = conn.cursor()
print("Database Connected Successfully")

#Used once to create the database
def init():
    db.execute('''CREATE TABLE WEATHER
(ID INT PRIMARY KEY NOT NULL,
DATE TEXT NOT NULL,
BEARING INT,
WINDSPEED REAL,
TEMPURATURE REAL);''')
    print("Table Created Sucessfully")

#INSERTING Data into the Database, function used requires Units:
##date - string, bearing - int in degrees, windspeed - float in m/s, tempurature - float in degrees Celsius
def insert_data(date, bearing, windspeed, tempurature):
    db.execute("INSERT INTO WEATHER VALUES ('"+ db.lastrowid+ "+ "+ date+ "'+ "+ bearing+ "+ "+ windspeed+ "+ "+ tempurature+ ");")
    db.commit()

#GETTING records from database and returning them in the form of tuples
##If function receives positive number, will return latest x entries
##If function receives negative number, will return first x entries
##If given string with date information, will return records relating to that date entry
#JUST HERE FOR GIT TO FORCE UPDATE
def get_records(index=0):
    rows = ()

    table = {}

    if(index > 0):
        rows = db.execute("SELECT * FROM WEATHER ORDER BY ID DESC LIMIT "+ str(index) + ";")
    if (index < 0):
        rows = db.execute("SELECT * FROM WEATHER ORDER BY ID ASC LIMIT "+ str(index) + ";")

    print(rows)

    for row in rows:
        table['id'] = row[0]
        table['date'] = row[1]
        table['bearing'] = row[2]
        table['windspeed'] = row[3]
        table['tampurature'] = row[4]

    json_table = json.dumps(table)

    return json_table

#Closes the database, please use or esle will throw errors and create problems
def close():
    db.commit()
    db.close()