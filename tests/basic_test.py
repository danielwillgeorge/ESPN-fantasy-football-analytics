import unittest
from api import teams

"""Tests for ESPN-fantasy-football-analytics."""


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_is_teams_success(self):
        self.assertTrue(teams())


if __name__ == '__main__':
    unittest.main()