import random

def play_martingale(starting_bet, starting_bankroll, max_spins, max_loss_streak):
    bankroll = starting_bankroll
    bet = starting_bet
    spins = 0
    loss_streak = 0
    while spins < max_spins and bet <= bankroll:
        result = random.choice(['red', 'black'])
        if result == 'black':
            bankroll += bet
            bet = starting_bet
            loss_streak = 0
        else:
            bankroll -= bet
            bet *= 2
            loss_streak += 1
            if loss_streak >= max_loss_streak:
                break
        spins += 1
    return bankroll

starting_bet = 1
starting_bankroll = 255
max_spins = 100
max_loss_streak = 8

results = []
for i in range(1000):
    final_bankroll = play_martingale(starting_bet, starting_bankroll, max_spins, max_loss_streak)
    results.append(final_bankroll)

print(f"Average final bankroll: ${sum(results) / len(results):,.2f}")
print(f"Number of bankruptcies: {results.count(0)}")
