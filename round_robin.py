import json

# a list of teams
even_teams = ['A', 'B', 'C', 'D']
odd_teams = ['A', 'B', 'C', 'D', 'E']

# a dictionary of games
games = {}

# determine # of teams
even_number_teams = len(even_teams)
odd_number_teams = len(odd_teams)

# if odd #, then add a 'bye' team
if odd_number_teams % 2 != 0:
    odd_teams.append('BYE')
    odd_number_teams = len(odd_teams)

# algorithm to determine # of games required for round robin
even_number_games = int((even_number_teams / 2) * (even_number_teams - 1))
odd_number_games = int((odd_number_teams / 2) * (odd_number_teams - 1))

print(even_teams)
print("Even # Teams: ", even_number_teams)
print("Even # Games: ", even_number_games)

print(odd_teams)
print("Odd # Teams: ", odd_number_teams)
print("Odd # Games: ", odd_number_games)

matches = [(team, opp)
           for team in even_teams
           for opp in even_teams
           if team != opp] * 1

print(matches)




