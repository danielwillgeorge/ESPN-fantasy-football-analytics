import unittest
import sys
import pandas as pd

sys.path.append("/Users/daniel.george/Desktop/github/ESPN-fantasy-football-analytics/fantasy-football-analytics")

import espnfantasyfootball
from espnfantasyfootball.api import teams

#from api import teams

"""Tests for ESPN-fantasy-football-analytics."""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_is_teams_success(self):
        self.assertIsInstance(teams(), pd.DataFrame)


if __name__ == '__main__':
    unittest.main()