import MySQLdb
import csv
import subprocess

# @Author Daniel George

matchups = [('Denver Broncos','Kansas City Chiefs'),
            ('New England Patriots','Buffalo Bills'),
            ('Tennessee Titans','Cleveland Browns'),
            ('Houston Texans','Carolina Panthers'),
            ('Arizona Cardinals','Chicago Bears'),
            ('San Diego Chargers','Cincinnati Bengals'),
            ('Detroit Lions','Minnesota Vikings'),
            ('Tampa Bay Buccaneers','New Orleans Saints'),
            ('Atlanta Falcons','New York Giants'),
            ('San Francisco 49ers','Pittsburgh Steelers'),
            ('St. Louis Rams','Washington Redskins'),
            ('Baltimore Ravens','Oakland Raiders'),
            ('Miami Dolphins','Jacksonville Jaguars'),
            ('Dallas Cowboys','Philadelphia Eagles'),
            ('Seattle Seahawks','Green Bay Packers'),
            ('New York Jets','Indianapolis Colts')]

for matchup in matchups:

	conn = MySQLdb.connect(db="Daniel", user="root", host="localhost", passwd="AmqsFyR0")
	curs = conn.cursor()
	curs.execute("""
	SELECT *
	FROM nfl_games
	WHERE home_team IN (%s,%s)
	AND visit_team IN (%s,%s)
	""", [matchup[0], matchup[1], matchup[0], matchup[1]]
	)

	data = curs.fetchall()

	with open('scores.csv','a') as csvfile:
		wr = csv.writer(csvfile,delimiter=',')
		for line in data:
			wr.writerow(line)