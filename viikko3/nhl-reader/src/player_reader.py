import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        res = requests.get(url).json()
        players = []

        for player_dc in res:
            player = Player(
                player_dc['name'],
                player_dc["team"],
                player_dc["goals"],
                player_dc["assists"],
                player_dc["nationality"]
            )

            players.append(player)

        self.players = players