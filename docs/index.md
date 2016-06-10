# Welcome to Fantasy Football Analytics' Documentation!

# Installation

This part of the documentation covers the installation of ESPN Fantasy Football Analytics.  The first step to using any good software pacakage
is making sure it is properly installed.

# Pip Install espnfantasyfootball

To install ESPN Fantasy Football Analytics, run this simple command in your terminal of choice:

    $ pip install espnfantasyfootball
    
# Quickstart

Eager to get started?  This section gives a good introduction in how to get started with ESPN Fantasy Football Analytics.

# Teams

Getting a list of NFL teams with ESPN Fantasy Football Analytics is very simple.

Begin by importing ESPN Fantasy Football Analytics:

    >>> import espnfantasyfootball as espn
    
Now, let's get a list of teams!  Easy as:

    >>> espn.teams()
    
*Parameters*: there are no required parameters for the `teams()` method.

`Teams` *Resource*: Here are the properties that appear in a `teams` resource:
- team: the official NFL team name of a team.
- abbrev: an abbreviation of the team name.
- url: the location of that team on http://www.espn.com/.

    
						    abbrev                                                          url
	   team                                                                                    
	   Dallas Cowboys          dal        http://espn.go.com/nfl/team/_/name/dal/dallas-cowboys
	   New York Giants         nyg       http://espn.go.com/nfl/team/_/name/nyg/new-york-giants
	   Philadelphia Eagles     phi   http://espn.go.com/nfl/team/_/name/phi/philadelphia-eagles
	   Washington Redskins     wsh   http://espn.go.com/nfl/team/_/name/wsh/washington-redskins
	   Buffalo Bills           buf         http://espn.go.com/nfl/team/_/name/buf/buffalo-bills
	   Miami Dolphins          mia        http://espn.go.com/nfl/team/_/name/mia/miami-dolphins
	   New England Patriots     ne   http://espn.go.com/nfl/team/_/name/ne/new-england-patriots
	   New York Jets           nyj         http://espn.go.com/nfl/team/_/name/nyj/new-york-jets
	   Arizona Cardinals       ari     http://espn.go.com/nfl/team/_/name/ari/arizona-cardinals
	   Los Angeles Rams         la       http://espn.go.com/nfl/team/_/name/la/los-angeles-rams
	   San Francisco 49ers      sf    http://espn.go.com/nfl/team/_/name/sf/san-francisco-49ers
	   Seattle Seahawks        sea      http://espn.go.com/nfl/team/_/name/sea/seattle-seahawks
	   Denver Broncos          den        http://espn.go.com/nfl/team/_/name/den/denver-broncos
	   Kansas City Chiefs       kc     http://espn.go.com/nfl/team/_/name/kc/kansas-city-chiefs
	   Oakland Raiders         oak       http://espn.go.com/nfl/team/_/name/oak/oakland-raiders
	   San Diego Chargers       sd     http://espn.go.com/nfl/team/_/name/sd/san-diego-chargers
	   Chicago Bears           chi         http://espn.go.com/nfl/team/_/name/chi/chicago-bears
	   Detroit Lions           det         http://espn.go.com/nfl/team/_/name/det/detroit-lions
	   Green Bay Packers        gb      http://espn.go.com/nfl/team/_/name/gb/green-bay-packers
	   Minnesota Vikings       min     http://espn.go.com/nfl/team/_/name/min/minnesota-vikings
	   Baltimore Ravens        bal      http://espn.go.com/nfl/team/_/name/bal/baltimore-ravens
	   Cincinnati Bengals      cin    http://espn.go.com/nfl/team/_/name/cin/cincinnati-bengals
	   Cleveland Browns        cle      http://espn.go.com/nfl/team/_/name/cle/cleveland-browns
	   Pittsburgh Steelers     pit   http://espn.go.com/nfl/team/_/name/pit/pittsburgh-steelers
	   Atlanta Falcons         atl       http://espn.go.com/nfl/team/_/name/atl/atlanta-falcons
	   Carolina Panthers       car     http://espn.go.com/nfl/team/_/name/car/carolina-panthers
	   New Orleans Saints       no     http://espn.go.com/nfl/team/_/name/no/new-orleans-saints
	   Tampa Bay Buccaneers     tb   http://espn.go.com/nfl/team/_/name/tb/tampa-bay-buccaneers
	   Houston Texans          hou        http://espn.go.com/nfl/team/_/name/hou/houston-texans
	   Indianapolis Colts      ind    http://espn.go.com/nfl/team/_/name/ind/indianapolis-colts
	   Jacksonville Jaguars    jax  http://espn.go.com/nfl/team/_/name/jax/jacksonville-jaguars
	   Tennessee Titans        ten      http://espn.go.com/nfl/team/_/name/ten/tennessee-titans
	
# Games

We can get a list of games for a given calendar year, too.  Again, super-easy.  This method takes one argument, the calendar year of your choice
expressed as an integer:

    >>> espn.games(2015)
    
*Parameters*: year: an integer value representing the calendar year for which you would like to retrieve game data.

`Games` *Resource*: Here are the properties that appear in a `games` resource:
- id: a unique identifier for that game on ESPN.com.

- date: the date the game took place, expressed in the format YYYY-mm-dd.

- home_team:

- home_team_score:

- visit_team:

- visit_team_score:
    
    				    date             home_team home_team_score            visit_team visit_team_score
	   id                                                                                                
	   400791590  2015-09-13        Dallas Cowboys              27       New York Giants               26
	   400791705  2015-09-20   Philadelphia Eagles              10        Dallas Cowboys               20
	   400791491  2015-09-27        Dallas Cowboys              28       Atlanta Falcons               39
	   400791720  2015-10-04    New Orleans Saints              26        Dallas Cowboys               20
	   400791559  2015-10-11        Dallas Cowboys               6  New England Patriots               30
	   400791564  2015-10-25       New York Giants              27        Dallas Cowboys               20
	   400791681  2015-11-01        Dallas Cowboys              12      Seattle Seahawks               13
	   400791734  2015-11-08        Dallas Cowboys              27   Philadelphia Eagles               33
	   400791494  2015-11-15  Tampa Bay Buccaneers              10        Dallas Cowboys                6
	   400791703  2015-11-22        Miami Dolphins              14        Dallas Cowboys               24
	   400791509  2015-11-26        Dallas Cowboys              14     Carolina Panthers               33
	   400791686  2015-12-07   Washington Redskins              16        Dallas Cowboys               19
	   400791612  2015-12-13     Green Bay Packers              28        Dallas Cowboys                7
	   400791656  2015-12-19        Dallas Cowboys              16         New York Jets               19
	   400791535  2015-12-27         Buffalo Bills              16        Dallas Cowboys                6
	   400791651  2015-01-03        Dallas Cowboys              23   Washington Redskins               34
	   400791786  2015-08-13    San Diego Chargers              17        Dallas Cowboys                7
	   400791787  2015-08-23   San Francisco 49ers              23        Dallas Cowboys                6
	   400791783  2015-08-29        Dallas Cowboys              14     Minnesota Vikings               28
	   400791777  2015-09-03        Dallas Cowboys              21        Houston Texans               14
	   400791672  2015-09-20       New York Giants              20       Atlanta Falcons               24
	   400791484  2015-09-24       New York Giants              32   Washington Redskins               21
	   400791678  2015-10-04         Buffalo Bills              10       New York Giants               24
	   400791584  2015-10-11       New York Giants              30   San Francisco 49ers               27
	   400791676  2015-10-19   Philadelphia Eagles              27       New York Giants                7
	   400791618  2015-11-01    New Orleans Saints              52       New York Giants               49
	   400791731  2015-11-08  Tampa Bay Buccaneers              18       New York Giants               32
	   400791591  2015-11-15       New York Giants              26  New England Patriots               27
	   400791506  2015-11-29   Washington Redskins              20       New York Giants               14
	   400791572  2015-12-06       New York Giants              20         New York Jets               23
	   ...               ...                   ...             ...                   ...              ...
	   
# Players

You can also retrieve data for players in the games.  This method takes one argument: an id from a `game` resource.

    >>> players(400554447)

*Parameters*: id: a long value representing the id for which you would like to retrieve player data.

`Players` *Resource*: Here are the properties that appear in a `players` resource:
- id: a unique identifier for the game on ESPN.com.

- team:

- gamepackage:

- player:

- REC:

- CAR:

- C/ATT:

- YDS:

- AVG:

- TD:

- LONG:

- TGTS:

- INT:

- SACKS:

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
		0   400554447            Seattle   receiving       Luke Willson   3             139  46.3  2   80    3          
		1   400554447            Seattle   receiving       Doug Baldwin   7             113  16.1  0   49   11          
		2   400554447            Seattle   receiving    Paul Richardson   5              52  10.4  0   22    7          
		3   400554447            Seattle   receiving      Bryan Walters   1              13  13.0  0   13    1          
		4   400554447            Seattle   receiving      Cooper Helfet   2               9   4.5  0    6    4          
		5   400554447            Seattle   receiving    Jermaine Kearse   1               8   8.0  0    8    1          
		6   400554447            Seattle   receiving   Ricardo Lockette   2               5   2.5  0    5    2          
		7   400554447  Arizona Cardinals   receiving         John Brown   3              54  18.0  0   24    8          
		8   400554447  Arizona Cardinals   receiving      Michael Floyd   2              41  20.5  0   32    8          
		9   400554447  Arizona Cardinals   receiving   Larry Fitzgerald   4              33   8.3  0   16   12          
		10  400554447  Arizona Cardinals   receiving       Darren Fells   2              26  13.0  0   15    2          
		11  400554447  Arizona Cardinals   receiving     Stepfan Taylor   2              25  12.5  0   18    3          
		12  400554447  Arizona Cardinals   receiving       John Carlson   2              15   7.5  0   12    3          
		13  400554447  Arizona Cardinals   receiving        Rob Housler   1              13  13.0  0   13    1          
		14  400554447  Arizona Cardinals   receiving        Jaron Brown   1               6   6.0  0    6    2          
		15  400554447  Arizona Cardinals   receiving       Marion Grice   1               3   3.0  0    3    4          
		16  400554447  Arizona Cardinals   receiving       Ted Ginn Jr.   0               0   0.0  0    0    2         

