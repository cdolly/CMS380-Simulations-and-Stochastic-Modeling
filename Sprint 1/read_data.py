"""
More Calculations problem for Sprint 1
Cameron Dolly

"""
import math
import matplotlib.pyplot as plt


def calc_mean(values):
  """
  Calculate the mean of a given list of values
  input is a list of float
  output the mean of those floats
  """
  sum = 0
  for x in values:
    sum = sum + x
  return sum / len(values)


def calc_median(values):
  """
  Calculate the median of a given list of values
  input is a list of float
  output the median of those floats
  """
  values.sort()
  middle = len(values) // 2
  return (values[middle] + values[~middle]) / 2


def calc_variance(values):
  """
  Calculate the variance of a given list of values
  input is a list of float
  output the variance of those floats
  """
  variance = 0
  mean = calc_mean(values)
  total = 0
  distFromMean = []
  for i in values:
    distFromMean.append((i - mean) * (i - mean))

  for i in distFromMean:
    total += i
  variance = total / len(distFromMean)
  return variance


def calc_standard_deviation(values):
  """
  Calculate the standard deviation of a given list of values
  input is a list of float
  output the standard deviation of those floats
  """
  return math.sqrt(calc_variance(values))


f = open('data.txt', 'r')

data = []

for line in f:
  data.append(float(line))

data_mean = calc_mean(data)
#print(data_mean)

data_median = calc_median(data)
#print(data_median)

data_variance = calc_variance(data)
#print(data_variance)

data_standard_deviation = calc_standard_deviation(data)
#print(data_standard_deviation)

plt.figure()
plt.hist(data, 20)
plt.title("Histogram of Data")
plt.xlabel("Data Value")
plt.ylabel("Count")
plt.savefig('histogram.pdf', bbox_inches='tight')

plt.figure()
plt.boxplot(data)
plt.title("Boxplot of Data")
plt.ylabel("Value")
plt.savefig('boxplot.pdf', bbox_inches='tight')
