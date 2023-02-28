import random

def simulate_boarding(num_seats):
    # Initialize the list of seats to be all empty
    seats = []
    for i in range(num_seats):
        seats.append(False)
    
    # Choose a random seat for the first passenger
    first_passenger_seat = random.randint(0, num_seats-1)
    
    # Mark the first passenger's seat as taken
    seats[first_passenger_seat] = True
    
    # Loop over the remaining passengers
    for passenger in range(1, num_seats):
        # Get the passenger's assigned seat number
        assigned_seat = passenger
        
        # Check if the passenger's assigned seat is empty
        if seats[assigned_seat-1] == False:
            # If the assigned seat is empty, sit there
            seats[assigned_seat-1] = True
        else:
            # If the assigned seat is already taken, choose a random empty seat
            empty_seats = []
            for i in range(num_seats):
                if seats[i] == False:
                    empty_seats.append(i)
            random_empty_seat = random.choice(empty_seats)
            seats[random_empty_seat] = True
            
    # Check if passenger 100 got her assigned seat
    return seats[num_seats-1]
    
# Run the simulation 10,000 times and compute the fraction of times passenger 100 gets her assigned seat
num_simulations = 10000
num_successes = 0
for i in range(num_simulations):
    if simulate_boarding(100):
        num_successes += 1
print("Probability of Passenger 100 getting her assigned seat:", num_successes / num_simulations)
