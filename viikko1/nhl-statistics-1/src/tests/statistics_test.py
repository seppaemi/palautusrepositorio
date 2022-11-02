import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [ 
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_find_player(self):
        name = self.statistics.search("Kurri")
        self.assertAlmostEqual(str(name), "Kurri EDM 37 + 53 = 90")

    def test_finds_none_if_no_player(self):
        name = self.statistics.search("test")
        self.assertAlmostEqual(name, None)

    def test_team_amount_correct(self):
        players = self.statistics.team("DET")
        players_amount = len(players)
        self.assertAlmostEqual(players_amount, 1)

    def test_find_correct_top_scorers(self):
        scorers = self.statistics.top(4)
        self.assertAlmostEqual(len(scorers), 4)
