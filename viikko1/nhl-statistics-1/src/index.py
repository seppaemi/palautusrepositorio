from player_reader import PlayerReader
from statistics import Statistics

def main():
    reader = PlayerReader()
    players = reader.get_players()
    statistics = Statistics(PlayerReader())
    philadelphia_flyers_players = statistics.team("PHI")
    top_scorers = statistics.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

if __name__ == "__main__":
    main()