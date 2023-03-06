"""
Ticket Program


"""
import random


def simulate():

  # Initialize a list of empty seats
  seats = [0] * 100
  # Assign seat 1 to passenger 1
  seats[0] = 1
  # Loop through passengers 2 to 100
  for i in range(2, 101):
    assignedSeat = i - 1
    if seats[assignedSeat - 1] == 0:  # If assigned seat is unoccupied
      seats[assignedSeat - 1] = i
    else:  # If assigned seat is occupied, find another unoccupied seat
      emptySeats = []
      for j in range(100):
        if seats[j] == 0:
          emptySeats.append(j)
      currentSeat = random.choice(emptySeats)
      seats[currentSeat] = i
  # Check if passenger 100 sits in her assigned seat
  if seats[99] == 100:
    return True
  else:
    return False


# Run the simulation for a large number of trials (100,000 in this case)
trials = 1000
successes = 0
for i in range(trials):
  if simulate():
    successes += 1

# Calculate the estimated probability that the 100th passenger gets her assigned seat
probability = successes / trials

# Print the estimated probability
print("Probability that passenger 100 gets to sit in seat 100:", probability)
