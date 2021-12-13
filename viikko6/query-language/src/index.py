from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn, Not, Or
from query_builder import QueryBuilder

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # Vähintään 30 maalia tai 50 syöttöä
    # matcher = Or(
    #     HasAtLeast(30, "goals"),
    #     HasAtLeast(50, "assists")
    # )

    # matcher = And(
    #     HasAtLeast(40, "points"),
    #     Or(
    #         PlaysIn("NYR"),
    #         PlaysIn("NYI"),
    #         PlaysIn("BOS")
    #     )
    # )

    # matcher = All()
    query = QueryBuilder()

    # matcher = query.playsIn("NYR").build()
    # matcher = (
    #     query
    #         .playsIn("NYR")
    #         .hasAtLeast(5, "goals")
    #         .hasFewerThan(10, "goals")
    #         .build()
    # )

    matcher = (
        query
            .oneOf(
            query.playsIn("PHI")
                .hasAtLeast(10, "assists")
                .hasFewerThan(5, "goals")
                .build(),
            query.playsIn("EDM")
                .hasAtLeast(40, "points")
                .build()
        )
        .build()
    )


    # matcher = query.oneOf(m1, m2).build()
    # matcher = query.playsIn("NYR").build()#.playsIn("NYR").build()



    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()
