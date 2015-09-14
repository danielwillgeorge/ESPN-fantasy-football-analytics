import MySQLdb
import csv
import subprocess

# @Author Daniel George

t = ('Detroit Lions','San Diego Chargers')

conn = MySQLdb.connect(db="Daniel", user="root", host="localhost", passwd="AmqsFyR0")
curs = conn.cursor()
curs.execute("""
SELECT *
FROM nfl_games
WHERE home_team IN (%s,%s)
AND visit_team IN (%s,%s)
""", [t[0], t[1], t[0], t[1]]
)

data = curs.fetchall()


with open('scores.csv','w') as csvfile:
	wr = csv.writer(csvfile,delimiter=',')
	for line in data:
		wr.writerow(line)