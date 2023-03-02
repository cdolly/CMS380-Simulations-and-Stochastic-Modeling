"""
Ticket Program


"""
import random


def simulate():
  # Initialize the list of seats to be all empty
  numSeats = 100
  currentPassenger = 0
  seats = []
  for i in range(numSeats):
    seats.append(-1)

  # Choose a random seat for the first passenger
  currentSeat = random.randint(0, numSeats - 1)

  # Mark the first passenger's seat as taken
  seats[currentSeat] = currentPassenger
  currentPassenger += 1
  currentSeat = 0
  assigning = True
  # Loop over the remaining passengers
  while (assigning == True):
    # If all 100 passengers have been assigned, exit the loop
    if (currentPassenger > 100):
      break

    # Check if the passenger's assigned seat is empty
    if seats[currentSeat] == -1:
      # If the assigned seat is empty, sit there
      seats[currentSeat] = currentPassenger
    else:
      # If the assigned seat is already taken, choose a random empty seat
      for i in range(numSeats):
        randomSeat = random.randint(0, numSeats - 1)
        if seats[randomSeat] == -1:
          seats[randomSeat] = currentPassenger
          break
    currentPassenger += 1
    currentSeat += 1

    # Check if passenger 100 got her assigned seat
  if (seats[numSeats - 1] == 100):
    return True
  else:
    return False


# Run the simulation 10,000 times and compute the fraction of times passenger 100 gets her assigned seat
simulations = 10000
successes = 0
for i in range(simulations):
  if simulate() == True:
    successes += 1
print("Probability of Passenger 100 getting her assigned seat:",
      successes / simulations)
