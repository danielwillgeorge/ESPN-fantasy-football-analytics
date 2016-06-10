![alt tag](https://circleci.com/gh/danielwillgeorge/ESPN-fantasy-football-analytics.png?circle-token=:circle-token)

# ESPN Fantasy Football Analytics Demo

A way to quickly retrieve ESPN team, game, and player data for a strategic edge in Fantasy Football leagues.

    >>> import espnfantasyfootball as espn
    >>> espn.teams()
    
						 abbrev                                                          url
	team                                                                                    
	Dallas Cowboys          dal        http://espn.go.com/nfl/team/_/name/dal/dallas-cowboys
	New York Giants         nyg       http://espn.go.com/nfl/team/_/name/nyg/new-york-giants
	Philadelphia Eagles     phi   http://espn.go.com/nfl/team/_/name/phi/philadelphia-eagles
	Washington Redskins     wsh   http://espn.go.com/nfl/team/_/name/wsh/washington-redskins
	Buffalo Bills           buf         http://espn.go.com/nfl/team/_/name/buf/buffalo-bills
    ...                     ...                                                          ...

    >>> espn.games(2015)
    
					 date             home_team home_team_score            visit_team visit_team_score
	id                                                                                                
	400791590  2015-09-13        Dallas Cowboys              27       New York Giants               26
	400791705  2015-09-20   Philadelphia Eagles              10        Dallas Cowboys               20
	400791491  2015-09-27        Dallas Cowboys              28       Atlanta Falcons               39
	400791720  2015-10-04    New Orleans Saints              26        Dallas Cowboys               20
	400791559  2015-10-11        Dallas Cowboys               6  New England Patriots               30
	...               ...                   ...             ...                   ...              ...

    >>> espn.players(400791590)
    
			   id               team gamepackage             player REC CAR  C/ATT  YDS   AVG TD LONG TGTS INT SACKS
	0   400554447            Seattle     passing     Russell Wilson          20/31  339  10.9  2             0  1-10
	1   400554447            Seattle     passing   Tarvaris Jackson            1/1    0   0.0  0             0   0-0
	2   400554447  Arizona Cardinals     passing       Ryan Lindley          18/44  216   4.9  0             1  4-29
	3   400554447  Arizona Cardinals     passing       Logan Thomas            0/1    0   0.0  0             0   0-0
	0   400554447            Seattle     rushing     Marshawn Lynch      10         113  11.3  2   79               
	1   400554447            Seattle     rushing     Russell Wilson       6          88  14.7  1   55               
	2   400554447            Seattle     rushing      Robert Turbin      10          38   3.8  0   11               
	3   400554447            Seattle     rushing  Christine Michael       8          28   3.5  0   15               
	4   400554447  Arizona Cardinals     rushing     Stepfan Taylor      11          19   1.7  0    4               
	5   400554447  Arizona Cardinals     rushing       Marion Grice       1           6   6.0  0    6               
	6   400554447  Arizona Cardinals     rushing   Kerwynn Williams       2           4   2.0  0    3               
	7   400554447  Arizona Cardinals     rushing      Robert Hughes       1           0   0.0  0    0
	...       ...                ...         ...                ... ... ...    ...  ...   ... ..  ...  ... ...   ...

# Setup

Simply:

    pip install espnfantasyfootball

# Troubleshoot/FAQ
