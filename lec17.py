
import sqlite3
import sys
import csv

#url = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv'
f = open("2011_february_us_airport_traffic.csv")
csv_data = csv.reader(f)
#for row in csv_data:
#    print(row)

conn = sqlite3.connect('AirportDB.sqlite')
cur = conn.cursor()

statement = '''
        DROP TABLE IF EXISTS 'AirportInfo';
    '''
cur.execute(statement)

statement = '''
	CREATE TABLE 'AirportInfo' (
		'iata' TEXT NOT NULL,
		'airport' TEXT NOT NULL,
		'city' TEXT NOT NULL,
		'state' TEXT NOT NULL,
		'country' TEXT NOT NULL,
		'lat' TEXT NOT NULL,
		'long' TEXT NOT NULL,
		'cnt' TEXT NOT NULL)'''
cur.execute(statement)

for (i, row) in enumerate(csv_data):
	if i == 0:
		continue
	insertation = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
	statement = 'INSERT INTO "AirportInfo" '
	statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
	cur.execute(statement, insertation)

statement = '''
        SELECT * FROM AirportInfo WHERE iata = "DTW";
    '''
result = cur.execute(statement)
print(result.fetchall())


conn.commit()
conn.close()