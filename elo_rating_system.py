# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 10:09:44 2020

@author: Walter

Trying out the Elo rating system
"""

# use number for random numbers
import numpy as np


def calc_elo_rating(player):
    if player['wins'] + player['losses'] == 0:
        player['rating'] = 1000
    else:
        player['rating'] = (player['points'] + 400 * (player['wins'] - player['losses'])) // (player['wins'] + player['losses'])
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
            player1, player2 = adjust_ratings(winner=player1,loser=player2)
    elif player1['skill'] < player2['skill']:
        player2, player1 = adjust_ratings(winner=player2,loser=player1)
    
    # do nothing for a tie
    
    return player1, player2
    

# Create the random players with random skills
total_players = 10000
players_to_keep = 10

players = [{'id': str(i).zfill(4), 
            'skill': i, # Just a basic number to sort by
            'wins':0, 
            'losses':0, 
            'points': 0, 
            'rating':1000} 
           for i in range(total_players)]

match_history = []

total_games = 0
while(len(players) > players_to_keep):
    for i in range(len(players)):
        total_games += 1
        
        j = np.random.randint(len(players))
        while (i,j) in match_history or i == j:
            j = np.random.randint(len(players))    
            
        match_history.append((i,j))

        # play_game will adjust the ratings of the players
        # based on who won or lost some skill based event
        players[i], players[j] = play_game(players[i], players[j])    

    players = sorted(players, key=lambda p:p['rating'])
    
    # drop the lowest 20% from the league
    indexes_to_drop = len(players) // 2
    # always keep 10
    indexes_to_drop = min(len(players) - 10, indexes_to_drop)
    
    print("Removing Players")
    for i in range(10):
        print(players[i])
        
    players = players[indexes_to_drop:]
               

# print out the top players and the total games played
players = sorted(players, key=lambda p:p['rating'])

print("Best Players")
for p in players:
    print(p)
print("total_games", total_games)
