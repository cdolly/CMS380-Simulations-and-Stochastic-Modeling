"""
Write a simulation to estimate the probability of winning at passe dix

Roll three 6-sided dice
Player wins if the sum is > 10
"""
#Basic strategy: Write a simulate function that plays 1 round of the game, and returns True if the player wins and False otherwise

#The main part of the program will call simulate() function in a loop and count the number of simulated trials that return true

# The fraction of wins approximates the true winning probability
from random import randint


def simulate():
  dice1 = randint(1, 6)
  dice2 = randint(1, 6)
  dice3 = randint(1, 6)

  sum = dice1 + dice2 + dice3

  if sum > 10:
    return True
  return False


### Main

num_trials = 10000
wins = 0
for i in range(num_trials):
  won = simulate()
  if won == True:
    wins += 1

winPercent = wins / num_trials
print('%.4f' % (winPercent * 100))
print("Games Played: " + str(num_trials))
