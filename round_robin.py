import json

# a list of teams
even_teams = ['A', 'B', 'C', 'D']
odd_teams = ['A', 'B', 'C', 'D', 'E']

# a dictionary of games
games = {}

even_number_teams = len(even_teams)
odd_number_teams = len(odd_teams)

if odd_number_teams % 2 != 0:
    odd_teams.append('BYE')
    odd_number_teams = len(odd_teams)

# algorithm to determine # of games required for round robin
even_number_games = (even_number_teams / 2) * (even_number_teams - 1)
odd_number_games = (odd_number_teams / 2) * (odd_number_teams - 1)

home_teams = even_teams[0:int(even_number_teams/2)]
away_teams = even_teams[int(even_number_teams/2):]

print(even_teams)
print(home_teams)
print(away_teams)
print("Even # Teams: ", even_number_teams)
print("Even # Games: ", even_number_games)

print(odd_teams)
print("Odd # Teams: ", odd_number_teams)
print("Odd # Games: ", odd_number_games)

num = 1
for home in home_teams:
    for away in away_teams:
        new = {"Game_" + str(num): home + " vs " + away}
        games.update(new)
        num = num + 1

print(games)

