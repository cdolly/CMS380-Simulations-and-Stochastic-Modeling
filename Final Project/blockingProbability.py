"""
Final Project 
Cameron Dolly
"""
from heapq import heappush, heappop, heapify
from math import log, factorial
from statistics import mean
from random import random

def erlang_b(m, e):
    # Input: m, number of servers and e, the traffic intensity
    # returns: the blocking probability
  numerator = (e ** m) / factorial(m)
  denominator = sum([(e ** i) / factorial(i) for i in range(m + 1)])
  return numerator / denominator


def rand_exp(rate):
    """ Generate an exponential random variate
        input: rate, the parameter of the
        distribution
        returns: the exponential variate
    """
    return -log(random()) / rate

def erlang_service_rate():
  """
  function to retrieve the erlang rate
  """
  total = rand_exp(1/.5) + rand_exp(1/.5)
  return total

def simulate(arrival_rate, num_servers, service_type):
    """ Simulate the M/M/1 queue, discrete-event style
        input: arrival_rate  the system's arrival rate
        returns: the average simulated residence time
    """
    # Stopping condition
    max_num_arrivals = 50000

    # Basic parameters
    service_rate = 1.0
    time = 0.0
    num_in_queue = 0
    num_blocked = 0
    num_arrivals = 0
   
    # Simulation data lists
    arrival_times = []
    enter_service_times = []
    departure_times = []

    # Initialize FEL as an empty list
    fel = []

   
    # Make the first arrival event
    interarrival_time = rand_exp(arrival_rate)
    new_event = (time + interarrival_time, 'arrival')
   
    # Insert with a heap operation
    heappush(fel, new_event)
   
    while len(fel) > 0 and num_arrivals < max_num_arrivals:
       
        # Pop the next event with a heap operation
        event = heappop(fel)
       
        # Event attributes
        event_time = event[0]
        event_type = event[1]
       
        # Advance simulated time
        time = event_time
       
        ### Processesing the events
       
        # If event type is arrival
        if event_type == 'arrival':
            num_arrivals += 1
            # added for multiple servers
            if num_in_queue < num_servers:
           
              # Log arrival time
              arrival_times.append(time)
             
              # Increment queue size
              num_in_queue += 1
             
              # Generate next arrival
              interarrival_time = rand_exp(arrival_rate)
              new_event = (time + interarrival_time, 'arrival')
              heappush(fel, new_event)
             
              # If queue was not empty and the number in the queue is less than the number of servers, enter service and generate a future departure event
              if num_in_queue <= num_servers and num_in_queue > 0:
                 
                  # Log enter service time
                  enter_service_times.append(time)
                 
                  # Generate new departure event
                  if service_type == False:
                    service_time = rand_exp(service_rate)
                  else:
                    service_time = erlang_service_rate()
                  new_event = (time + service_time, 'departure')
                  heappush(fel, new_event)
            else:
              # Generate next arrival for server
              num_blocked += 1
              interarrival_time = rand_exp(arrival_rate)
              new_event = (time + interarrival_time, 'arrival')
              heappush(fel, new_event)
             
             
        # If event is a departure
        elif event_type == 'departure':
           
            # Log departure time
            departure_times.append(time)
           
            # Decrement queue size
            num_in_queue -= 1
           
            # If there are more customers waiting, put the next one into service and generate a departure
            if num_in_queue >= num_servers:
               
                # Log enter service time
                enter_service_times.append(time)
               
                # Generate new departure event
                if service_type == False:
                  service_time = rand_exp(service_rate)
                else:
                  service_time = erlang_service_rate()
                new_event = (time + service_time, 'departure')
                heappush(fel, new_event)

    return num_blocked/num_arrivals # ratio
   



trials = []

print("Trial with service rate = 1")
# Trials with service rate 1
# 13 servers
for trial in range(5):
    trials.append(simulate(10, 13, False))

print("Simulated Average of 13 servers:", mean(trials))
print("Erlang-B with 13 Servers:", erlang_b(13, 10))
trials = []

 # 18 servers
for trial in range(5):
    trials.append(simulate(10, 18, False))

print("Simulated Average of 18 servers:", mean(trials))
print("Erlang-B with 18 Servers:", erlang_b(18, 10))
trials = []

# 21 servers
for trial in range(5):
    trials.append(simulate(10, 21, False))

print("Simulated Average of 21 servers:", mean(trials))
print("Erlang-B with 21 Servers:", erlang_b(21, 10))
trials = []


#2-stage Erlang Distribution Service Rate trial
print("Trials w/ 2-stage Erlang Distribution Service Rate")
 
for i in range(10, 21):
    for trial in range(5):
        trials.append(simulate(10, i, True))

    print("Blocking Rate for", i, " servers:", mean(trials))

