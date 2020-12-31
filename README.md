# Elo Rating Algorithm
This is a basic implementation of the Elo rating system for creating league rankings. 

This was created to help rank different sets of neural network weights against each other while evolving them to do a skill based task. The top performers then are saved and used to create the next generation of weights for the neural network. 

https://en.wikipedia.org/wiki/Elo_rating_system


## Simple Example Tournament with Elo ratings

This example create 100 players with skill levels of 0-99. Skills in the example are simple an integer. If one player's skill (integer) is higher than the other, that player wins.
After each round in the tournament, 20% of the lowest players are dropped.
At the end of the tournament, only the highest skilled players remain. 

In this example of 100 players, players with skills 90-99 make it to the top 10.

### Example output from the script

```python
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
```
