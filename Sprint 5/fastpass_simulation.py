from heapq import heappush, heappop, heapify
from random import random
from math import log
import matplotlib.pyplot as plt


def rand_exp(rate):
  return -log(random()) / rate


def simulate(arrival_rate, fraction_fastpass):
  # Stopping condition
  max_num_arrivals = 5000
  # Basic parameters
  service_rate = 1.0
  time = 0.0
  num_in_queue_regular = 0
  num_in_queue_fastpass = 0
  # Simulation data lists
  arrival_times_regular = []
  arrival_times_fastpass = []
  enter_service_times_regular = []
  enter_service_times_fastpass = []
  departure_times_regular = []
  departure_times_fastpass = []
  # Initialize FEL as an empty list
  fel = []

  # Make the first arrival event
  interarrival_time = rand_exp(arrival_rate)
  num = random()
  if (num < fraction_fastpass):
    # 0 means the customer is fastpass
    priority = (0, time + interarrival_time)
  else:
    # 1 means the customer is non-fastpass
    priority = (1, time + interarrival_time)
  new_event = (priority, 'arrival')

  # Insert with a heap operation
  heappush(fel, new_event)

  while (len(fel) > 0) and (len(arrival_times_regular) +
                            len(arrival_times_fastpass)) < max_num_arrivals:
    # Pop the next event with a heap operation
    event = heappop(fel)

    # Event attributes
    event_priority = event[0]
    event_type = event[1]

    # Advance simulated time
    time = event_priority[1]
    #-------------------------------------------------------------------------------------------------------------------
    ### Process events
    # Arrivals
    # If event is arrival and fastpass
    if event_type == 'arrival' and event_priority[0] == 0:

      # Log arrival time
      arrival_times_fastpass.append(time)

      # Increment queue size
      num_in_queue_fastpass += 1

      # Generate next arrival
      interarrival_time = rand_exp(arrival_rate)
      num = random()
      if (num < fraction_fastpass):
        # 0 means the customer is fastpass
        priority = (0, time + interarrival_time)
      else:
        # 1 means the customer is non-fastpass
        priority = (1, time + interarrival_time)
      new_event = (priority, 'arrival')
      # Put new arrival into heap
      heappush(fel, new_event)

      # If queue was empty, enter service and generate a future departure event
      if num_in_queue_fastpass == 1:

        # Log enter service time
        enter_service_times_fastpass.append(time)

        # Generate new departure event
        service_time = rand_exp(service_rate)
        priority = (0, time + service_time)
        new_event = (priority, 'departure')
        heappush(fel, new_event)
#------------------------------------------------------------------------------
# If event is departure and fastpass
    elif event_type == 'departure' and event_priority[0] == 0:

      # Log departure time
      departure_times_fastpass.append(time)

      # Decrement queue size
      num_in_queue_fastpass -= 1

      # If there are more customers waiting, put the next one into service and generate a departure
      if num_in_queue_fastpass > 0:

        # Log enter service time
        enter_service_times_fastpass.append(time)

        # Generate new departure event
        service_time = rand_exp(service_rate)
        priority = (0, time + service_time)
        new_event = (priority, 'departure')
        heappush(fel, new_event)

#------------------------------------------------------------------------------
# If event is arrival and non-fastpass
    elif event_type == 'arrival' and event_priority[0] == 1:

      # Log arrival time
      arrival_times_regular.append(time)

      # Increment queue size
      num_in_queue_regular += 1

      # Generate next arrival
      interarrival_time = rand_exp(arrival_rate)
      num = random()
      if (num < fraction_fastpass):
        # 0 means the customer is fastpass
        priority = (0, time + interarrival_time)
      else:
        # 1 means the customer is non-fastpass
        priority = (1, time + interarrival_time)
      new_event = (priority, 'arrival')
      # Put new arrival into heap
      heappush(fel, new_event)

      # If queue was empty, with noone in fastpass queue, enter service and generate a future departure event
      if (num_in_queue_regular == 1) and (num_in_queue_fastpass == 0):

        # Log enter service time
        enter_service_times_regular.append(time)

        # Generate new departure event
        service_time = rand_exp(service_rate)
        priority = (1, time + service_time)
        new_event = (priority, 'departure')
        heappush(fel, new_event)
#------------------------------------------------------------------------------
# If event is departure and non-fastpass
    elif event_type == 'departure' and event_priority[0] == 1:

      # Log departure time
      departure_times_regular.append(time)

      # Decrement queue size
      num_in_queue_regular -= 1

      # If there are more customers waiting, put the next one into service and generate a departure
      if num_in_queue_regular > 0:

        # Log enter service time
        enter_service_times_regular.append(time)

        # Generate new departure event
        service_time = rand_exp(service_rate)
        priority = (1, time + service_time)
        new_event = (priority, 'departure')
        heappush(fel, new_event)
#------------------------------------------------------------------------------
# End of loop

# End of Simulation

# Calculate statistics
# For regular customers
  residence_time_regular = [
    departure_times_regular[i] - arrival_times_regular[i]
    for i in range(len(departure_times_regular))
  ]
  average_residence_time_regular = sum(residence_time_regular) / len(
    residence_time_regular)

  # For fastpass customers
  if (fraction_fastpass == 0):
    return average_residence_time_regular, 0
  residence_time_fastpass = [
    departure_times_fastpass[i] - arrival_times_fastpass[i]
    for i in range(len(departure_times_fastpass))
  ]
  average_residence_time_fastpass = sum(residence_time_fastpass) / len(
    residence_time_fastpass)

  return average_residence_time_regular, average_residence_time_fastpass


###############################################################################################

# Calculating residence times with lamba = 0.95 / high load
# Calculating residence times with varying values of fraction_fastpass
arrival_rate = 0.95
fraction_fastpass = 0.00
high_load_residence_times_fastpass = {}
high_load_residence_times_regular = {}

while fraction_fastpass <= 1.0:
  sim_residence_times_regular = []
  sim_residence_times_fastpass = []

  for i in range(20):
    result = simulate(arrival_rate, fraction_fastpass)
    sim_residence_times_regular.append(result[0])
    sim_residence_times_fastpass.append(result[1])

  r_avg_regular = sum(sim_residence_times_regular) / len(
    sim_residence_times_regular)
  r_avg_fastpass = sum(sim_residence_times_fastpass) / len(
    sim_residence_times_fastpass)

  high_load_residence_times_regular[fraction_fastpass] = r_avg_regular
  high_load_residence_times_fastpass[fraction_fastpass] = r_avg_fastpass

  fraction_fastpass += 0.05

plt.plot(high_load_residence_times_fastpass.keys(),
         high_load_residence_times_fastpass.values())
plt.plot(high_load_residence_times_regular.keys(),
         high_load_residence_times_regular.values())
plt.xlabel("Fraction of Fastpass Customers")
plt.ylabel("Simulated Average Residence Time (m)")
plt.legend(["Regular", "Fastpass"], loc="lower right")
plt.title("Fraction of Fastpass Customers Vs Avg. Residence Time @ High Load")
plt.savefig('HighloadResidenceTimes.pdf')
plt.clf()

#---------------------------------------------------------------------------------------------
# Calculating residence times with lamba = 0.50 / low load
# Calculating residence times with varying values of fraction_fastpass
arrival_rate = 0.50
fraction_fastpass = 0.00
high_load_residence_times_fastpass = {}
high_load_residence_times_regular = {}

while fraction_fastpass <= 1.0:
  sim_residence_times_regular = []
  sim_residence_times_fastpass = []

  for i in range(20):
    result = simulate(arrival_rate, fraction_fastpass)
    sim_residence_times_regular.append(result[0])
    sim_residence_times_fastpass.append(result[1])

  r_avg_regular = sum(sim_residence_times_regular) / len(
    sim_residence_times_regular)
  r_avg_fastpass = sum(sim_residence_times_fastpass) / len(
    sim_residence_times_fastpass)

  high_load_residence_times_regular[fraction_fastpass] = r_avg_regular
  high_load_residence_times_fastpass[fraction_fastpass] = r_avg_fastpass

  fraction_fastpass += 0.05

plt.plot(high_load_residence_times_fastpass.keys(),
         high_load_residence_times_fastpass.values())
plt.plot(high_load_residence_times_regular.keys(),
         high_load_residence_times_regular.values())
plt.xlabel("Fraction of Fastpass Customers")
plt.ylabel("Simulated Average Residence Time (m)")
plt.legend(["Regular", "Fastpass"], loc="lower right")
plt.title("Fraction of Fastpass Customers Vs Avg. Residence Time @ Low Load")
plt.savefig('LowloadResidenceTimes.pdf')
