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
    
              id     team             player CAR  YDS   AVG TD LONG
    0  400554447  Seattle     Marshawn Lynch  10  113  11.3  2   79
    1  400554447  Seattle     Russell Wilson   6   88  14.7  1   55
    2  400554447  Seattle      Robert Turbin  10   38   3.8  0   11
    3  400554447  Seattle  Christine Michael   8   28   3.5  0   15

# Setup

Simply:

    pip install espnfantasyfootball

# Troubleshoot/FAQ
