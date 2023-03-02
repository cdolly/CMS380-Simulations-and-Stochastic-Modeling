"""
Martingale Problem

"""
import random
import matplotlib.pyplot as plt


def simulate(startingBet, startingBankroll, maxSpins, maxLossStreak):
  bankroll = startingBankroll
  bet = startingBet
  spins = 0
  lossStreak = 0
  netgain = 0

  while spins < maxSpins and bet <= bankroll:
    result = random.choice(['red', 'black'])

    if result == 'black':
      bankroll += bet
      netgain += bet
      bet = startingBet
      lossStreak = 0

    else:
      bankroll -= bet
      netgain -= bet
      bet *= 2
      lossStreak += 1
      if lossStreak >= maxLossStreak:
        break
    spins += 1

  return netgain


startingBet = 1
startingBankroll = 255
maxSpins = 100
maxLossStreak = 8

gameResults = []
for i in range(1000):
  finalBankroll = simulate(startingBet, startingBankroll, maxSpins,
                           maxLossStreak)
  gameResults.append(finalBankroll)

plt.figure()
plt.hist(gameResults, 20)
plt.title("Histogram of Game Results")
plt.xlabel("Net Gain of Bankroll")
plt.ylabel("Count")
plt.savefig('histogram.pdf', bbox_inches='tight')
