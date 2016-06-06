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


def teams(teams=[], teams_urls=[], prefix_1=[], prefix_2=[]):
	url = "http://espn.go.com/nfl/teams"
	pd.set_option('display.width', 1000)
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
			prefix_1.append(url.split("/")[-2])
			prefix_2.append(url.split("/")[-1])
	dic = {"url": teams_urls, "prefix_2": prefix_2, "prefix_1": prefix_1}
	teams = pd.DataFrame(dic, index=teams)
	teams.index.name = "team"
	
	return teams
	

def games(year, match_id=[], dates=[], home_team=[], home_team_score=[], visit_team=[], visit_team_score=[], teams=teams):
    year = int(year)
    BASE_URL = "http://espn.go.com/nfl/team/schedule/_/name/{0}/year/{1}/{2}/seasontype/2"
    for index, row in teams().iterrows():
        _team, url = index, row['url']
        r = requests.get(BASE_URL.format(row['prefix_1'], year, row['prefix_2']))
        soup = BeautifulSoup(r.text, "html.parser")
        table = soup.find('table', {'class':'tablehead'})
            
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            try:
                _home = True if columns[2].li.text == 'vs' else False
                _other_team = columns[2].find_all('a')[1].text
                _score = columns[3].a.text.split(' ')[0].split('-')
                _won = True if columns[3].span.text == 'W' else False

                match_id.append(columns[3].a['href'].split('?gameId=')[1])
                home_team.append(_team if _home else _other_team)
                visit_team.append(_team if not _home else _other_team)
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


def players(year, players=[], stats=[], stats_=[], divs=[]):
    return None






class players(object):
    def __init__(self):
        self.paths = ['2014','2013','2012','2011','2010']
        self.BASE_URL = 'http://espn.go.com/nfl/boxscore?gameId={0}'

        self.players = []
        self.stats = []
        self.stats_ = []
        self.divs = []

        '''classes = ["col column-one gamepackage-away-wrap","col column-two gamepackage-home-wrap"]
            
            gamepackage-passing
            gamepackage-rushing
            gamepackage-receiving
            gamepackage-fumbles
            gamepackage-defensive
            gamepackage-interceptions
            gamepackage-kickReturns
            gamepackage-puntReturns
            gamepackage-kicking
            gamepackage-punting'''

    def get(self):
        for path in paths:
            #games = pd.read_csv('/path/to/' + path + '_games.csv')
            games(year)
            for index, row in games.iterrows():
                id = row['id']
                r = requests.get(BASE_URL.format(id))
                soup = BeautifulSoup(r.text, "html.parser")
                table = soup.find_all('div', {'id':'gamepackage-rushing'}) # Replace the "id" parameter with one of the strings
                														   # from the triple-quotes above. 
                for table_ in table:
                    table_ = table_.find_all('div', {'class':'col column-two gamepackage-home-wrap'}) # Replace the "class" parameter with one of the strings from
                																					  # the commented-out "classes" list above.  This will return one
                																					  # set of data at a time; otherwise, the request will time out
                																					  # (in my experience).	
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
                                    self.stats.append(id)
                                    self.stats.append(row.caption.text[:(len(row.caption.text)-8)])
                                    for i in range(0,6):
                                    #adjust to (0,7) for passing and receiving pulls
                                        self.stats.append(cols[i].text)
                                        self.stats_.append(stats)
            self.statistics = pd.DataFrame(np.array(stats_), columns=columns)
            self.players = players.append(statistics)
            # Replace "rushing" with the stats you are looking at (passing, receiving, etc.).
            # This will return a csv with half of the total data
            # (for either the home or visiting team).  Run the script again
            # changing the variables, for the other half.
        players.to_csv(path + '_rushing_.csv')