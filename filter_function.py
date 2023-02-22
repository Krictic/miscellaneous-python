# filter()
# Syntax: filter(function, iterable)

games_scores = \
    [("Ultra Kaiju Monster Rancher", 91, "JRPG"),
     ("Steerising", 90, "RPG"),
     ("Ghost Trick: Phantom Detective", 97, "Adventure"),
     ("Resident Evil 3: nemesis", 96, "Survival Horror"),
     ("Dynasty Warriors 9 Empires", 95, "Strategy"),
     ("Starcraft", 91, "Strategy"),
     ("Jak 3", 88, "Adventure"),
     ("Gradius V", 88, "Shooter"),
     ("Total Annihilation", 86, "Strategy"),
     ("Battlefront (2004)", 76, "Shooter"),
     ("Beyond Good and Evil", 87, "Adventure"),
     ("SSX 3", 87, "Sports"),
     ("Megaman X5", 86, "Platformer"),
     ("Castlevania: SoN", 91, "Platformer")]


high_score = lambda data: data[1] >= 90
low_score = lambda data: data[1] < 90
strategy = lambda data: data[2] == "Strategy"
adventure = lambda data: data[2] == "Adventure"
shooter = lambda data: data[2] == "Shooter"
sports = lambda data: data[2] == "Sports"
survival_horror = lambda data: data[2] == "Survival Horror"

high = list(filter(high_score, games_scores))
low = list(filter(low_score, games_scores))
strategy_games = list(filter(strategy, games_scores))
adventure_games = list(filter(adventure, games_scores))
shooter_games = list(filter(shooter, games_scores))
sports_games = list(filter(sports, games_scores))
survival_games = list(filter(survival_horror, games_scores))


def game_genre(genre):
    for i in genre:
        print(i, end="\n")


for j in high:
    print(j, end=" ")

for r in low:
    print(j, end=" ")

game_genre(strategy_games)
game_genre(shooter_games)
game_genre(adventure_games)
game_genre(sports_games)
game_genre(survival_games)

