import unittest
import sys
import pandas as pd

import espnfantasyfootball
from espnfantasyfootball.api import teams, games, players

#sys.path.append("/Users/daniel.george/Desktop/github/ESPN-fantasy-football-analytics/fantasy-football-analytics")
#from api import teams

"""Tests for ESPN-fantasy-football-analytics."""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_is_teams_success(self):
        self.assertIsInstance(teams(), pd.DataFrame)
        
    def test_is_games_success(self):
        self.assertIsInstance(games(2015), pd.DataFrame)
        
    def test_is_players_success(self):
        self.assertIsInstance(players(400554447), pd.DataFrame)


if __name__ == '__main__':
    unittest.main()