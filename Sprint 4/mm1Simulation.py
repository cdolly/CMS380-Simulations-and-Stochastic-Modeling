"""
Sprint 4 M/M/1 Simulation 

Cameron Dolly
"""
from random import random
from math import log
import matplotlib.pyplot as plt
import statistics
import math
#--- Generate an exponential random variate
#
# Input: mu, the parameter of the exponential distribution
# Output: a value x drawn from the exponential distribution with rate mu
def rand_exp(mu):

    # Generates and returns an exponential RV
    return -log(random()) / mu

#--- Simulate the M/M/1 queue
#
# Inputs:
#    arrival_rate
#    avg_service_time
#    n: number of simulated customers
#
# Output: the average residence time of customer in the queue
def simulate(arrival_rate, avg_service_time, n):
    
    # Generate interarrival times
    # Uses rand_exp to generate n interarrival times with parameter arrival_rate
    interarrival_times = [0] * n
    for i in range(1, n):
        interarrival_times[i] = rand_exp(arrival_rate)
    #print(interarrival_times, 'Interarrival')

    # Generate service times
    # Uses rand_exp to generate n service times with parameter 1 / avg_service_time
    service_times = [0] * n
    for i in range(1,n):
        service_times[i] = rand_exp(1 / avg_service_time)
    #print(service_times, 'Service Times')

    # Calculate arrival times
    # Uses interarrival times to calculate a list of arrival times
    arrival_times = [0] * n
    total_time = 0
    for i in range(1,n):
        total_time = total_time + interarrival_times[i]
        arrival_times[i] = total_time
    #print(arrival_times, 'Arrival Times')

    # Initialize other lists
    enter_service_times = [0] * n
    departure_times = [0] * n
    
    # Setup for first arrival
    enter_service_times[0] = arrival_times[0]
    departure_times[0] = enter_service_times[0] + service_times[0]

    residence_times = [0] * n
    
    # Loop over all other arrivals
    for i in range(1, n):
        # Calculate enter_service_times[i]
        enter_service_times[i] = max(arrival_times[i], departure_times[i - 1])
        
        # Calculates departure_times[i]
        departure_times[i] = enter_service_times[i] + service_times[i]
        
    # Calculates list of residence times
        residence_times[i] = departure_times[i] - arrival_times[i]
    
    # Returns average residence time
    total_time = 0
    for i in residence_times:
        total_time += i
    avg_residence_time = total_time / len(residence_times)
    return avg_residence_time



arrival_rate = 0.05
n = 1000
avg_service_time = 1.0
total = 0
numbers = []
UCL_list = []
LCL_list = []
UCL_value = 0
LCL_value = 0
average_residence_times = {}
utilization_per_arrival_rate = {}

while arrival_rate < 0.96:
    
    for i in range (0,5):
        current_residence_time = simulate(arrival_rate, avg_service_time, n)
        total += current_residence_time
        numbers.append(current_residence_time)
        
    Y_bar = total / 5
    average_residence_times[arrival_rate] = Y_bar
    utilization_per_arrival_rate[arrival_rate] = arrival_rate * avg_service_time
    
    s = statistics.stdev(numbers)

    UCL = (Y_bar + ((2.776 * s) / math.sqrt(5)))
    LCL = (Y_bar - ((2.776 * s) / math.sqrt(5)))

    UCL_list.append(UCL)
    LCL_list.append(LCL)
    
    total = 0
    arrival_rate += 0.05

x = utilization_per_arrival_rate.values()
y = average_residence_times.values()

plt.plot(x, y)
plt.fill_between(x, (LCL_list), (UCL_list), color = 'b', alpha =0.1)
plt.xlabel("Utilization")
plt.ylabel("Simulated Average Residence Time")
plt.title("Utilization Vs Simulated Average Residence Time per Arrival Rate")
plt.savefig('mm1Simulation.pdf')
