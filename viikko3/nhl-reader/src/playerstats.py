import requests
from player import Player
from playerreader import PlayerReader

class PlayerStats:

    def __init__(self, reader):
    
        """
        Args:
            reader ([object]): A PlayerReader object
        """
        self.reader = reader
    
    def filter_by_nationality(self, players_list, nationality):
        """ Filters players by nationality """
        return list(filter(lambda x: x.nationality == nationality, players_list))
        
    def top_scorers_by_nationality(self, nationality):
        """ Top scorers by nation """
        players = self.reader.get_players()

        # Filter by nationality
        nationality_filtered = self.filter_by_nationality(players, nationality)

        # Sort by assists and goals
        nationality_filtered.sort()
        return nationality_filtered
