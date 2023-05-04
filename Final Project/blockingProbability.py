from math import factorial, log
from random import random
from heapq import heappush, heappop, heapify


def rand_exp(rate):
  return -log(random()) / rate


def ErlangB(m, E):
    num = ((E**m) / factorial(m))
    den = sum([(E**i) / factorial(i) for i in range(m + 1)]) 
    return (num / den)


def simulate(arrival_rate, avg_service_time, num_servers):
    # Stopping condition for simulation
    max_num_arrivals = 50
    max_num_customers = num_servers
    # Future Event list
    fel = []
    arrival_times = []
    departure_times = []
    # Count of customers that have been dropped due to exceded server limit
    num_blocked_customers = 0
    num_customers = 0
    time = 0.0
    total_arrivals = 0

    # Generate first arrival
    interarrival_time = rand_exp(arrival_rate)
    # Insert customer using heap method

    new_event = (time + interarrival_time,'arrival')
    total_arrivals += 1
    heappush(fel, new_event)

    # Begin loop
    while(len(fel) > 0 and (len(arrival_times)) <= max_num_arrivals):
        # Pop next event
        event = heappop(fel)

        # Assiging event attributes
        event_time = event[0]
        event_type = event[1]

        # Advance time
        time = event_time


        # Process events
        # If event type is an arrival
        if(event_type == 'arrival'):
            print('arrival')
            arrival_times.append(time)
            # Increment number of customers
            num_customers += 1

            # Process that customer and generate their departure time
            new_event = (time + rand_exp(avg_service_time), 'departure')
            heappush(fel,new_event)

            # Generate next arrival
            interarrival_time = rand_exp(arrival_rate)
            new_event = (time + interarrival_time,'arrival')
            total_arrivals += 1
            heappush(fel, new_event)

            # Enter service if space is available, otherwise drop
            if(num_customers <= num_servers):
                service_time = rand_exp(avg_service_time)
                new_event = (time + service_time, 'departure')
                heappush(fel, new_event)

            # If a customer arrives when there is no service space, drop them and generate departure at their arrival time
            elif(num_customers > num_servers):
                num_customers -= 1
                num_blocked_customers += 1
                new_event = (time, 'departure')
                heappush(fel, new_event)

        # If event type is a departure
        elif(event_type == 'departure'):
            print('departure')
            departure_times.append(time)
            num_customers -= 1
            

        print(num_customers)



    
    print('Total arrivals', total_arrivals)
    print('Blocked customers', num_blocked_customers)
    return num_blocked_customers / total_arrivals

            

        







arrival_rate = 10
avg_service_time = 1
num_servers = 13

result = simulate(arrival_rate,avg_service_time,num_servers)
print('13',result)

"""
num_servers = 17

result = simulate(arrival_rate,avg_service_time,num_servers)
print('17',result)


num_servers = 21

result = simulate(arrival_rate,avg_service_time,num_servers)
print('21',result)
"""
