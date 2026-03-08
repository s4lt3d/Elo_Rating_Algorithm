# Elo Rating Algorithm

> Python implementation of the Elo rating system for ranking agents in competitive tournaments with evolutionary selection.

---

## Overview

This project implements the [Elo rating system](https://en.wikipedia.org/wiki/Elo_rating_system) to rank competing agents (neural networks, game bots, etc.) through tournament play. The system is designed for **evolutionary selection**: top performers are preserved for the next generation while low performers are eliminated.

**Primary Use Case:** Train neural network populations by running tournaments, using Elo ratings to identify and preserve superior networks.

---

## How It Works

### Elo Rating Formula

```
rating = (points + 400 * (wins - losses)) / (wins + losses)
```

**Components:**
- **points** — Accumulated opponent ratings from each game
- **wins/losses** — Head-to-head record against other players
- **400** — K-factor controlling rating volatility
- **Base rating** — 1000 (starting point for new players)

### Tournament Flow

1. **Initialize population** — Create N agents with random weights (skill levels)
2. **Play tournament** — Agents compete in pairwise matches
3. **Elo update** — Calculate ratings for all players
4. **Elimination** — Remove bottom 20% of players by rating
5. **Next generation** — Keep top performers, create new agents from elite copies
6. **Repeat** — Run multiple tournament rounds until convergence

### Rating Dynamics

- **Winner gains** — Opponent's rating added to points
- **Loser gains** — Winner's rating added to points (still accumulates experience)
- **Strong opponents** — Beating higher-rated players builds rating faster
- **Consistent play** — Higher wins/losses ratio means more established rating

---

## Features

- **Fair Ranking** — Elo accounts for opponent strength, not just win count
- **Evolutionary Pressure** — Progressive elimination creates selection pressure
- **Flexible Win Conditions** — Define victory by any criterion (skill, network output, etc.)
- **Scalable** — Works with any population size
- **Simple Integration** — Easy to adapt for neural networks, game AI, or other agents

---

## Usage

### Basic Example

```bash
python elo_rating_system.py
```

### Running Your Own Tournament

```python
from elo_rating_system import calc_elo_rating, adjust_ratings, play_game

# Initialize players
players = [
    {'name': 'Agent_1', 'skill': 50, 'wins': 0, 'losses': 0, 'points': 0, 'rating': 1000},
    {'name': 'Agent_2', 'skill': 70, 'wins': 0, 'losses': 0, 'points': 0, 'rating': 1000},
    # ... more players
]

# Play tournament matches
for p1, p2 in match_pairs:
    p1, p2 = play_game(p1, p2)

# Sort by rating
players = sorted(players, key=lambda p: p['rating'], reverse=True)

# Elite players for next generation
elite = players[:top_k]
```

---

## Core Functions

### `play_game(player1, player2)`
Executes a single match between two players.
- Determines winner based on `skill` attribute
- Updates ratings via `adjust_ratings()`
- Handles ties (no rating change)

```python
player1, player2 = play_game(player1, player2)
```

### `adjust_ratings(winner, loser)`
Updates Elo ratings and stats after a match.
- Adds opponent rating to winner's points
- Adds opponent rating to loser's points (experience)
- Increments wins/losses
- Recalculates rating

```python
winner, loser = adjust_ratings(winner, loser)
```

### `calc_elo_rating(player)`
Calculates current Elo rating from points and record.
- Handles zero-game edge case (returns 1000)
- Used after each match to update rating

```python
player = calc_elo_rating(player)
```

### `create_shuffle(length)`
Generates a derangement: permutation where no element is in original position.
- Ensures players don't play themselves
- Used to create match pairings

```python
shuffle = create_shuffle(100)
```

### `generate_random_name()`
Creates random pronounceable names for agents.

---

## Example Output

The included example creates 100 agents with skill levels 0-99. After tournament rounds with 20% elimination:

```
Best Players
{'name': 'Vebuga', 'skill': 99, 'wins': 24, 'losses': 0, 'points': 33635, 'rating': 1801}
{'name': 'Pucobe', 'skill': 98, 'wins': 22, 'losses': 2, 'points': 34359, 'rating': 1764}
{'name': 'Ladeha', 'skill': 95, 'wins': 22, 'losses': 2, 'points': 33524, 'rating': 1730}
{'name': 'Kunoki', 'skill': 96, 'wins': 21, 'losses': 3, 'points': 34236, 'rating': 1726}
{'name': 'Lahudo', 'skill': 97, 'wins': 22, 'losses': 2, 'points': 32767, 'rating': 1698}
...
```

**Observation:** Agents with highest skill (95-99) naturally rise to top 10 through Elo ranking.

---

## Customization

### For Neural Networks

```python
# Replace 'skill' with network evaluation
def play_game(nn1, nn2):
    # Evaluate both networks on benchmark
    score1 = nn1.evaluate(benchmark)
    score2 = nn2.evaluate(benchmark)

    winner = nn1 if score1 > score2 else nn2
    loser = nn2 if score1 > score2 else nn1

    return adjust_ratings(winner, loser)
```

### For Game AI

```python
# Use game match results
def play_game(bot1, bot2):
    result = run_game(bot1, bot2)
    winner = bot1 if result == 1 else bot2
    loser = bot2 if result == 1 else bot1

    return adjust_ratings(winner, loser)
```

### Adjust K-Factor

Modify the rating formula in `calc_elo_rating()` to change volatility:

```python
# More volatile (changes faster)
rating = (points + 800 * (wins - losses)) / (wins + losses)

# More stable (changes slower)
rating = (points + 200 * (wins - losses)) / (wins + losses)
```

---

## Applications

- **Neural Network Evolution** — Evolve populations through tournament selection
- **Game AI Training** — Rank bots and create improved generations
- **Hyperparameter Tuning** — Test configurations against each other
- **Benchmark Comparison** — Fair ranking of agents by actual performance

---

## Mathematical Properties

- **Zero-sum system** — Points distributed equally (winner gains opponent rating)
- **Self-correcting** — Good players build rating faster against weak players
- **Stable over time** — Ratings converge as players accumulate matches
- **Fair ordering** — Higher rating = higher expected win rate

---

## License

Copyright © Walter Gordy
