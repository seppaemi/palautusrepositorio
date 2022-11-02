from player_reader import PlayerReader
from statistics import Statistics
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def main():
    statistics = Statistics(PlayerReader())
    philadelphia_flyers_players = statistics.team("PHI")
    top_scorers = statistics.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)
    
    print("Top point goal scorers:")
    for player in statistics.top(10, SortBy.GOALS.value):
        print(player)

    print("Top by assists:")
    for player in statistics.top(10, SortBy.ASSISTS.value):
        print(player)

if __name__ == "__main__":
    main()