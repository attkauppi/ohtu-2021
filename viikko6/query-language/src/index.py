from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, HasFewerThan, PlaysIn, Not, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # Vähintään 30 maalia tai 50 syöttöä
    # matcher = Or(
    #     HasAtLeast(30, "goals"),
    #     HasAtLeast(50, "assists")
    # )

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )


    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()
