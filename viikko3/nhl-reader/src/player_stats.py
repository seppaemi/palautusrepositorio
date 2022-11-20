class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            filter(lambda player: player.nationality == nationality,
                   self.reader.players
            ),
            key=lambda player: player.goals+player.assists,
            reverse=True
        )