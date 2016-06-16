# -*- coding: utf-8 -*-

"""
ESPN-analytics.api
~~~~~~~~~~~~

This module implements the ESPN-analytics API.

__author__ = "Daniel George"
__license__ = MIT, see LICENSE.txt for more details.

"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date

dic_ = {'dallas-cowboys':'Dallas Cowboys',
'cowboys':'Dallas Cowboys',
'new-york-giants':'New York Giants',
'giants':'New York Giants',
'philadelphia-eagles':'Philadelphia Eagles',
'eagles':'Philadelphia Eagles',
'washington-redskins':'Washington Redskins',
'redskins':'Washington Redskins',
'buffalo-bills':'Buffalo Bills',
'bills':'Buffalo Bills',
'miami-dolphins':'Miami Dolphins',
'dolphins':'Miami Dolphins',
'new-england-patriots':'New England Patriots',
'patriots':'New England Patriots',
'new-york-jets':'New York Jets',
'jets':'New York Jets',
'arizona-cardinals':'Arizona Cardinals',
'cardinals':'Arizona Cardinals',
'los-angeles-rams':'Los Angeles Rams',
'rams':'Los Angeles Rams',
'san-francisco-49ers':'San Francisco 49ers',
'49ers':'San Francisco 49ers',
'seattle-seahawks':'Seattle Seahawks',
'seahawks':'Seattle Seahawks',
'denver-broncos':'Denver Broncos',
'broncos':'Denver Broncos',
'kansas-city-chiefs':'Kansas City Chiefs',
'chiefs':'Kansas City Chiefs',
'oakland-raiders':'Oakland Raiders',
'raiders':'Oakland Raiders',
'san-diego-chargers':'San Diego Chargers',
'chargers':'San Diego Chargers',
'chicago-bears':'Chicago Bears',
'bears':'Chicago Bears',
'detroit-lions':'Detroit Lions',
'lions':'Detroit Lions',
'green-bay-packers':'Green Bay Packers',
'packers':'Green Bay Packers',
'minnesota-vikings':'Minnesota Vikings',
'vikings':'Minnesota Vikings',
'baltimore-ravens':'Baltimore Ravens',
'ravens':'Baltimore Ravens',
'cincinnati-bengals':'Cincinnati Bengals',
'bengals':'Cincinnati Bengals',
'cleveland-browns':'Cleveland Browns',
'browns':'Cleveland Browns',
'pittsburgh-steelers':'Pittsburgh Steelers',
'steelers':'Pittsburgh Steelers',
'atlanta-falcons':'Atlanta Falcons',
'falcons':'Atlanta Falcons',
'carolina-panthers':'Carolina Panthers',
'panthers':'Carolina Panthers',
'new-orleans-saints':'New Orleans Saints',
'saints':'New Orleans Saints',
'tampa-bay-buccaneers':'Tampa Bay Buccaneers',
'buccaneers':'Tampa Bay Buccaneers',
'houston-texans':'Houston Texans',
'texans':'Houston Texans',
'indianapolis-colts':'Indianapolis Colts',
'colts':'Indianapolis Colts',
'jacksonville-jaguars':'Jacksonville Jaguars',
'jaguars':'Jacksonville Jaguars',
'tennessee-titans':'Tennessee Titans',
'titans':'Tennessee Titans'}

classes = ["col column-one gamepackage-away-wrap","col column-two gamepackage-home-wrap"]

gamepackages = ['gamepackage-passing', 'gamepackage-rushing', 'gamepackage-receiving']

pd.set_option('display.width', 1200)


def teams(teams=[], teams_urls=[], abbrev=[]):
	url = "http://espn.go.com/nfl/teams"
	pd.set_option('display.width', 1000)
	pd.set_option('display.max_colwidth', 1000)
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	tables = soup.find_all("ul", class_="medium-logos")

	for table in tables:
		lis = table.find_all("li")
		for li in lis:
			info = li.h5.a
			url = info["href"]
			teams.append(info.text)
			teams_urls.append(url)
			abbrev.append(url.split("/")[-2])
	dic = {"url": teams_urls, "abbrev": abbrev}
	teams = pd.DataFrame(dic, index=teams)
	teams.index.name = "team"
	
	return teams
	

def games(year, match_id=[], dates=[], home_team=[], home_team_score=[], visit_team=[], visit_team_score=[], teams=teams):
    year = int(year)
    BASE_URL = "http://espn.go.com/nfl/team/schedule/_/name/{0}/year/{1}/{2}/seasontype/2"
    for index, row in teams().iterrows():
        _team, url = index, row['url']
        r = requests.get(BASE_URL.format(row['abbrev'], year, row['url'].split("/")[-1]))
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', {'class':'tablehead'})
            
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            try:
                _home = True if columns[2].li.text == 'vs' else False
                _other_team = columns[2].find_all('a')[1]['href'].split('/')[-1]
                _score = columns[3].a.text.split(' ')[0].split('-')
                _won = True if columns[3].span.text == 'W' else False

                match_id.append(columns[3].a['href'].split('?gameId=')[1])
                home_team.append(_team if _home else dic_[_other_team])
                visit_team.append(_team if not _home else dic_[_other_team])
                d = datetime.strptime(columns[1].text, '%a, %b %d')
                dates.append(date(year, d.month, d.day))

                if _home:
                    if _won:
                        home_team_score.append(_score[0])
                        visit_team_score.append(_score[1])
                    else:
                        home_team_score.append(_score[1])
                        visit_team_score.append(_score[0])
                else:
                    if _won:
                        home_team_score.append(_score[1])
                        visit_team_score.append(_score[0])
                    else:
                        home_team_score.append(_score[0])
                        visit_team_score.append(_score[1])
            except Exception as e:
                pass # Not all columns row are a match, is OK
            
    dic = {'id': match_id, 'date': dates, 'home_team': home_team, 'visit_team': visit_team,
    'home_team_score': home_team_score, 'visit_team_score': visit_team_score}
    games = pd.DataFrame(dic).drop_duplicates(subset='id').set_index('id')
    return games

def group_(seq, size):
  return (seq[pos:pos + size] for pos in xrange(0, len(seq), size))

def players(id):

	columns = ['id', 'team', 'gamepackage', 'player', 'REC', 'CAR', 'C/ATT', 'YDS', 'AVG', 'TD', 'LONG', 'TGTS', 'INT', 'SACKS']
	players_ = pd.DataFrame(columns=columns)

	columns = ['id', 'team', 'gamepackage', 'player', 'REC', 'CAR', 'C/ATT', 'YDS', 'AVG', 'TD', 'LONG', 'TGTS', 'INT', 'SACKS']
	_players = pd.DataFrame(columns=columns)

	BASE_URL = 'http://espn.go.com/nfl/boxscore?gameId={0}'

	for gamepackage in gamepackages:
		stats_ = []
		id = id
		r = requests.get(BASE_URL.format(id))
		soup = BeautifulSoup(r.text, "html5lib")
		title = soup.title.text.split(' ')
		
		for class_ in classes:
		
			table = soup.find_all('div', {'id':gamepackage})
			
			for table_ in table:
				table_ = table_.find_all('div', {'class':class_})
			
				for _row in table_:
					heads = _row.find_all('thead')
					for line in heads:
						headers = line.find_all('th')
						headers = [th.text for th in headers]
						headers.pop(0)
						columns = ['id', 'team', 'gamepackage', 'player'] + headers
						if gamepackage == 'gamepackage-rushing':
							columns = columns[:9]
						elif gamepackage == 'gamepackage-receiving':
							columns = columns[:10]
						else:
							columns = columns[:12]
						players = pd.DataFrame(columns=columns)
				
					rows = _row.find_all('td')
					
					if gamepackage == 'gamepackage-rushing':
						n = 6
					elif gamepackage == 'gamepackage-receiving':
						n = 7
					else:
						n = 9
				
					for group in group_(rows, n):
						stats = []
						stats.append(id)
						if class_ == 'col column-two gamepackage-home-wrap':
							stats.append(dic_[title[2].lower()])
						else:
							stats.append(dic_[title[0].lower()])
						stats.append(gamepackage.split('-')[-1])
						try:
							for i in range(0,n):
							#adjust to (0,7) for passing and receiving pulls
								if group[i].text == 'TEAM':
									break
								else:
									stats.append(group[i].text)
						except IndexError:
							pass
						if not len(stats) == 3:
							stats_.append(stats)

		
		statistics = pd.DataFrame(np.array(stats_), columns=columns)
		players = players.append(statistics)

		players_ = pd.concat([players_, players])

	res = players_.reindex_axis(_players.columns, axis=1)
	res = res.fillna('')
	res = res.set_index('id')
	res.index.name = 'id'

	return res