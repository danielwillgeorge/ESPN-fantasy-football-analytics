#import copper
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date
#copper.project.path = '../..'

#games = copper.read_csv('games.csv').set_index('id')
#games = pd.read_csv('/Users/daniel.george/Desktop/Github/espn-analytics/nfl/games.csv')
paths = ['2014','2013','2012','2011','2010']

BASE_URL = 'http://espn.go.com/nfl/boxscore?gameId={0}'

#http://espn.go.com/nba/boxscore?gameId=400277727
#http://espn.go.com/nfl/boxscore?gameId=400749514

# @Author Daniel George
# @Works Cited: Daniel Rodriguez, https://github.com/danielfrg/nba

players = []
stats = []
stats_ = []

classes = ["col column-one gamepackage-away-wrap","col column-two gamepackage-home-wrap"]
divs = []

#for item in classes:

for path in paths:
	games = pd.read_csv('/Users/daniel.george/Desktop/Github/espn-analytics/nfl/' + path + '_games.csv')
	for index, row in games.iterrows():
		id = row['id']
		r = requests.get(BASE_URL.format(id))
		soup = BeautifulSoup(r.text, "html.parser")
		table = soup.find_all('div', {'id':'gamepackage-rushing'})

		for table_ in table:
			table_ = table_.find_all('div', {'class':'col column-two gamepackage-home-wrap'})	


			for row in table_:
				heads = row.find_all('thead')
				for line in heads:
					headers = line.find_all('th')
					headers = [th.text for th in headers]
					headers.pop(0)
					columns = ['id', 'team', 'player'] + headers
					columns = columns[:8]
					#adjust to :9 for passing and receiving pulls
					players = pd.DataFrame(columns=columns)
							
				rows = row.find_all('tr', {'class':''})
				for row_ in rows:
					cols = row_.find_all('td')
					if not cols[1].text.startswith('DNP'):
						stats = []
						stats.append(id)
						stats.append(row.caption.text[:(len(row.caption.text)-8)])
						for i in range(0,6):
						#adjust to (0,7) for passing and receiving pulls
							stats.append(cols[i].text)
					stats_.append(stats)


	statistics = pd.DataFrame(np.array(stats_), columns=columns)
	players = players.append(statistics)
	players.to_csv(path + '_rushing_.csv')
		
				

# 	stats = stats[:11]
# 	for i in range(1):
# 		players.loc[i] = stats
# 	print players
			
				
				
# 			array = np.zeros((len(['Matthew Spafford']), 11), dtype=object)
# 			array[:]=np.nan
# 			array[0,1]=row.caption.text[:(len(row.caption.text)-8)]
# 			for i, player in enumerate(['Matthew Spafford']):
# 				cols = row.find_all('td')
# 				for j in range(0, 9):
# 					if not cols[1].text.startswith('DNP'):
# 						array[i,j+2] = cols[j].text
			
# 			players = players.append(frame)
# 			print players
# 			#players = players.append(frame)
# 			for x in array:
# 				line = np.concatenate((x, ['Detroit',index]))
# 				new = pd.DataFrame(line)
# # 				new = pd.DataFrame(line, columns=frame.columns)
# # 				frame = frame.append(new)
# 				players = players.append(new)



# 			bodies = table.tbody
# 			team_1_players = bodies[0].find_all('tr')
# 			print team_1_players
			
			
# 			array = np.zeros((2,9), dtype=object)
# 			array[:]=np.nan
# 			
# 			
# 			cols = row.find_all('td')
# 			for j in range(1, 9):
# 				if not cols[1].text.startswith('DNP'):
# 					print cols[j].text
								
				
				
# def get_players(players, team_name):
#     array = np.zeros((len(players), len(headers)+1), dtype=object)
#     array[:] = np.nan
#     for i, player in enumerate(players):
#         cols = player.find_all('td')
#         array[i, 0] = cols[0].text.split(',')[0]
#         for j in range(1, len(headers) + 1):
#             if not cols[1].text.startswith('DNP'):
#                 array[i, j] = cols[j].text
# 
#     frame = pd.DataFrame(columns=columns)
#     for x in array:
#         line = np.concatenate(([index, team_name], x)).reshape(1,len(columns))
#         new = pd.DataFrame(line, columns=frame.columns)
#         frame = frame.append(new)
#     return frame
# 
# for index, row in games.iterrows():
#     print(index)
#     request = requests.get(BASE_URL.format(index))
#     table = BeautifulSoup(request.text).find('table', class_='mod-data')
#     heads = table.find_all('thead')
#     bodies = table.find_all('tbody')
# 
#     team_1 = heads[0].th.text
#     team_1_players = bodies[0].find_all('tr') + bodies[1].find_all('tr')
#     team_1_players = get_players(team_1_players, team_1)
#     players = players.append(team_1_players)
# 
#     team_2 = heads[3].th.text
#     team_2_players = bodies[3].find_all('tr') + bodies[4].find_all('tr')
#     team_2_players = get_players(team_2_players, team_2)
#     players = players.append(team_2_players)
# 
# players = players.set_index('id')
# print(players)
# #copper.save(players, 'players')