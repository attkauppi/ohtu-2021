import requests
from player import Player
from playerstats import PlayerStats
from playerreader import PlayerReader

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"

    reader = PlayerReader(url)
    ps = PlayerStats(reader)
    players_by_nationality = ps.top_scorers_by_nationality("FIN")

    for player in players_by_nationality:
        print(player)

if __name__ == "__main__":
    main()
