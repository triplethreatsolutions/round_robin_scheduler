import json
import timeit

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

# make empty list to hold matches
matches = []

# determine # of times teams will play each other
number_plays = 1

for id in range (0, (1 * number_plays)):
    # copy registered teams for match generation algorithm
    teams = odd_teams[:]
    registered_teams = odd_teams[:]
    # match generation algorithm, single play only
    for team in registered_teams:
        for opp in teams:
            if opp != team:
                matches.append((team, opp))
        del teams[0]

print(matches)

for match in matches:
    if match[0] != 'BYE' and match[1] != 'BYE':
        print ("Home:" + match[0] + " vs Away: " + match[1])









