"""
Baccarat Simulation Game for Sprint 1
Cameron Dolly
"""
from random import randint

def simulate():
  """
  Simulates one round of the baccarat card game
  returns an int 0,1 or -1 depending on the result of the game.
  0 represents a a banker win, 1 represents a player win, and -1 represents a tie
  """
  # Generating cards for player
  playerCardOne = randint(1, 13)
  playerCardTwo = randint(1, 13)
  playerPoints = 0
  #  print(playerCardOne)
  #  print(playerCardTwo)

  # Generating cards for banker
  bankerCardOne = randint(1, 13)
  bankerCardTwo = randint(1, 13)
  bankerPoints = 0
  #  print(bankerCardOne)
  #  print(bankerCardTwo)

  # Logic for determining points awarded based on randomly generated cards for player
  if (playerCardOne > 0 and playerCardOne < 10) and (playerCardTwo > 0
                                                     and playerCardTwo < 10):
    playerPoints = (playerCardOne + playerCardTwo) % 10
  elif (playerCardOne > 0 and
        playerCardOne < 10) and not (playerCardTwo > 0 and playerCardTwo < 10):
    playerPoints = playerCardOne % 10
  elif not (playerCardOne > 0 and playerCardOne < 10) and (
      playerCardTwo > 0 and playerCardTwo < 10):
    playerPoints = playerCardTwo % 10

  # Logic for determining points awarded based on randomly generated cards for banker
  if (bankerCardOne > 0 and bankerCardOne < 10) and (bankerCardTwo > 0
                                                     and bankerCardTwo < 10):
    bankerPoints = (bankerCardOne + bankerCardTwo) % 10
  elif (bankerCardOne > 0 and
        bankerCardOne < 10) and not (bankerCardTwo > 0 and bankerCardTwo < 10):
    bankerPoints = bankerCardOne % 10
  elif not (bankerCardOne > 0 and bankerCardOne < 10) and (
      bankerCardTwo > 0 and bankerCardTwo < 10):
    bankerPoints = bankerCardTwo % 10

  # Logic to evaluate whether more cards need to be dealt or not
  # Tie by natural, player natural win, and banker natural win
  if (playerPoints >= 8) and (bankerPoints >= 8):
    return -1
  elif (playerPoints >= 8) and not (bankerPoints >= 8):
    return 1
  elif not (playerPoints >= 8) and (bankerPoints >= 8):
    return 0

  # Player point value of 0-5
  if (playerPoints <= 5):
    playerCardThree = randint(1, 13)
    if (playerCardThree <= 9):
      playerPoints = playerPoints + playerCardThree

    if (bankerPoints <= 2):
      bankerCardThree = randint(1, 13)
      if (bankerCardThree <= 9):
        bankerPoints = bankerPoints + bankerCardThree

    elif (bankerPoints == 3):
      if not (playerCardThree == 8):
        bankerCardThree = randint(1, 13)
        if (bankerCardThree <= 9):
          bankerPoints = bankerPoints + bankerCardThree

    elif (bankerPoints == 4):
      if (playerCardThree >= 2 and playerCardThree <= 7):
        bankerCardThree = randint(1, 13)
        if (bankerCardThree <= 9):
          bankerPoints = bankerPoints + bankerCardThree

    elif (bankerPoints == 5):
      if (playerCardThree >= 4 and playerCardThree <= 7):
        bankerCardThree = randint(1, 13)
        if (bankerCardThree <= 9):
          bankerPoints = bankerPoints + bankerCardThree

    elif (bankerPoints == 6):
      if (playerCardThree >= 6 and playerCardThree <= 7):
        bankerCardThree = randint(1, 13)
        if (bankerCardThree <= 9):
          bankerPoints = bankerPoints + bankerCardThree

  elif (playerPoints > 5):
    # Banker point value of 0-5
    if (bankerPoints <= 5):
      bankerCardThree = randint(1, 13)
      if (bankerCardThree <= 9):
        bankerPoints = bankerPoints + bankerCardThree

  # Evaluating scores at end of game
  if (playerPoints == bankerPoints):
    return -1
  elif (playerPoints > bankerPoints):
    return 1
  elif (bankerPoints > playerPoints):
    return 0


gamesPlayed = 10000
playerWins = 0
bankerWins = 0
ties = 0

for i in range(gamesPlayed):
  result = simulate()
  if (result == 0):
    bankerWins += 1
  elif (result == 1):
    playerWins += 1
  elif (result == -1):
    ties += 1

playerPercent = (playerWins / gamesPlayed) * 100
bankerPercent = (bankerWins / gamesPlayed) * 100
tiePercent = (ties / gamesPlayed) * 100

print(playerPercent)
print(bankerPercent)
print(tiePercent)
