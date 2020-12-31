# -*- coding: utf-8 -*-
"""
Simple Example Tournament with Elo ratings

This example create 100 players with skill levels of 0-99.
After each round in the tournament, 20% of the lowest players are dropped.
At the end of the tournament, only the highest skilled players remain. 
In the example of 100 players, players with skills 90-99 make the top 10

EXAMPLE OUTPUT

Best Players
{'name': 'Viciko', 'skill': 91, 'wins': 16, 'losses': 8, 'points': 34518, 'rating': 1571}
{'name': 'Dixuva', 'skill': 90, 'wins': 17, 'losses': 7, 'points': 33842, 'rating': 1576}
{'name': 'Defete', 'skill': 93, 'wins': 18, 'losses': 6, 'points': 33740, 'rating': 1605}
{'name': 'Lukiqo', 'skill': 94, 'wins': 18, 'losses': 6, 'points': 34582, 'rating': 1640}
{'name': 'Ripeba', 'skill': 92, 'wins': 20, 'losses': 4, 'points': 33604, 'rating': 1666}
{'name': 'Lahudo', 'skill': 97, 'wins': 22, 'losses': 2, 'points': 32767, 'rating': 1698}
{'name': 'Kunoki', 'skill': 96, 'wins': 21, 'losses': 3, 'points': 34236, 'rating': 1726}
{'name': 'Ladeha', 'skill': 95, 'wins': 22, 'losses': 2, 'points': 33524, 'rating': 1730}
{'name': 'Pucobe', 'skill': 98, 'wins': 22, 'losses': 2, 'points': 34359, 'rating': 1764}
{'name': 'Vebuga', 'skill': 99, 'wins': 24, 'losses': 0, 'points': 33635, 'rating': 1801}

"""

# using numpy for random numbers
import numpy as np
import random
import string


def calc_elo_rating(player):
    if player['wins'] + player['losses'] == 0:
        player['rating'] = 1000
    else:
        player['rating'] = (player['points'] + 400 * (player['wins'] -
                                                      player['losses'])) // (player['wins'] + player['losses'])
    return player


def adjust_ratings(winner, loser):
    winner['points'] += loser['rating']
    loser['points'] += winner['rating']

    winner['wins'] += 1
    loser['losses'] += 1

    winner = calc_elo_rating(winner)
    loser = calc_elo_rating(loser)

    return winner, loser


def play_game(player1, player2):

    if player1['skill'] > player2['skill']:
        player1, player2 = adjust_ratings(winner=player1, loser=player2)
    elif player1['skill'] < player2['skill']:
        player2, player1 = adjust_ratings(winner=player2, loser=player1)
    # do nothing for a tie

    return player1, player2

def create_shuffle(length):
    
    l = list(range(length))
    if length == 1:
        return l
    
    valid = False
    while valid == False:
        l = random.sample(l, length)
        for i in range(length):
            if l[i] == i:
                valid = False
                break
            valid = True
    
    return l
        

def generate_random_name():
    VOWELS = "aeiou"
    CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
    
    name = "".join([random.choice(CONSONANTS) if i%2==0 else random.choice(VOWELS) for i in range(6)])    
    return name.capitalize()

# Create 100 random players with progressive skill levels 
total_players = 100
players_to_keep = 10

players = [{'name': generate_random_name(),
            'skill': i,  # Just a basic number to sort by
            'wins': 0,
            'losses': 0,
            'points': 0,
            'rating': 1000}
           for i in range(total_players)]


# Here we start the tournament. 
# We eliminate 20% of the lowest players each round until only 10 players remain

total_games = 0
while(len(players) > players_to_keep):
    # Here we create the matches to play
    matches = []
    p2_random = create_shuffle(len(players))
    for p1_in_order in range(len(players)):
        matches.append((p1_in_order,p2_random[p1_in_order]))
    
    # Play the matches
    for match in matches:
        p1, p2 = match
        total_games += 1
        
        # play_game() will adjust the ratings of the players
        players[p1], players[p2] = play_game(players[p1], players[p2])

    # sort the players based on rating then remove bottom 20%
    players = sorted(players, key=lambda p: p['rating'])

    # drop the lowest 20% from the league
    indexes_to_drop = len(players) // 5
    # always keep at least 10
    indexes_to_drop = min(len(players) - 10, indexes_to_drop)

    players = players[indexes_to_drop:]


# print out the top players and the total games played
print("Best Players")
for p in players:
    print(p)
print("total_games", total_games)

