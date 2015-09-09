import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

# @Author Daniel George
# @Works Cited: Daniel Rodriguez, https://github.com/danielfrg/nba

paths = ['2014','2013','2012','2011','2010']

BASE_URL = 'http://espn.go.com/nfl/boxscore?gameId={0}'

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