"""
Campus Connections Problem for Sprint 1
Cameron Dolly

"""
# Standard matplotlib import
import matplotlib

matplotlib.use('Agg')
from matplotlib import pyplot as plt

# csv module makes it easy to process delimited text files
import csv


# Print the students in each course
def printClassStudent(dict):
  for course_id in dict:
    student_list = dict[course_id]
    print(course_id + ': ' + str(student_list))


# Print the courses each student is assigned to
def printStudentClass(dict):
  for student_id in dict:
    course_list = dict[student_id]
    print(student_id + ': ' + str(course_list))


#Finding mean class size
def calc_mean(dict):
  """
  Calculates mean number of students from the dictionary
  Input is a dictionary of student ID numbers
  Output is mean number of students
  """
  total = 0
  for course_id in dict:
    num = len(dict[course_id])
    total += num
  print('Mean:' + str(total / len(dict)))


#Finding median class size
def calc_median(dict):
  """
  Calculates median number of students from the dictionary
  Input is a dictionary of student ID numbers
  Output is median number of students
  """
  list = []
  for course_id in dict:
    list.append(len(dict[course_id]))

  list.sort()
  middle = len(list) // 2
  print('Median:' + str((list[middle] + list[~middle]) / 2))


def make_hist(dict):
  """
  Prints a histogram of student distrubution from the dictionary
  Input is a dictionary of student ID numbers
  Output is pdf of the histogram
  """
  plt.figure()
  list = []
  for course_id in dict:
    list.append(len(dict[course_id]))

  plt.hist(list, 20)
  plt.title("Histogram of Class Size")
  plt.xlabel("Class Size")
  plt.ylabel("Count")
  plt.savefig('ClassHist.pdf', bbox_inches='tight')


def make_boxplot(dict):
  """
  Prints a boxplot of student distrubution from the dictionary
  Input is a dictionary of student ID numbers
  Output is pdf of the boxplot
  """
  plt.figure()
  list = []
  for course_id in dict:
    list.append(len(dict[course_id]))

  plt.boxplot(list)
  plt.title("Boxplot of Class Size")
  plt.ylabel("Value")
  plt.savefig('ClassBoxplot.pdf', bbox_inches='tight')


def calc_interactions(courses_per_student, students_per_course):
  """
  Takes two dictionaries as input, one with student enrollment info, and the other with course enrollement info
  Outputs a dictionary of each student's ID and their unique number of interactions
  """
  uniqueInteractions = {}
  interactions = 0
  for student_id in courses_per_student:
    list = courses_per_student[student_id]

    for x in list:
      interactions += (len(students_per_course[x]) - 1)
    uniqueInteractions[student_id] = interactions
    interactions = 0

  return uniqueInteractions


def makeBoxplotInteractions(dict1, dict2):
  """
  Prints a boxplot of unique student interactions from the dictionary
  Input is both dictionaries, enrollement info and course info
  Output is pdf of the boxplot
  """
  interactions = calc_interactions(dict1, dict2)
  plt.figure()
  list = []
  for x in interactions:
    list.append(interactions[x])

  plt.boxplot(list)
  plt.title("Boxplot of Unique Number of Interactions")
  plt.ylabel("Value")
  plt.savefig('UniqueInteractionsBoxplot.pdf', bbox_inches='tight')


def makeHistogramInteractions(dict1, dict2):
  """
  Prints a histogram of unique number of student interactions
  Input is both dictionaries, enrollement info and course info
  Output is pdf of the histogram
  """
  interactions = calc_interactions(dict1, dict2)
  plt.figure()
  list = []
  for x in interactions:
    list.append(interactions[x])

  plt.hist(list, 20)
  plt.title("Histogram of Unique Number of Interactions")
  plt.xlabel("Number of Unique Interactions")
  plt.ylabel("Count")
  plt.savefig('UniqueInteractionsHistogram.pdf', bbox_inches='tight')


# Create an empty dictionary to record which students are in each course
students_per_course = {}
courses_per_student = {}

# Open the file and create a csv reader
f = open('enrollments.csv', 'r')
reader = csv.reader(f)

# Reader automatically iterates through the lines in the file
for line in reader:
  # csv reader automatically turns the line into a list of fields
  student_id = line[0]
  course_id = line[1]

  if course_id not in students_per_course:
    students_per_course[course_id] = []
  if student_id not in courses_per_student:
    courses_per_student[student_id] = []

  students_per_course[course_id].append(student_id)
  courses_per_student[student_id].append(course_id)

### Comment out which method you do not want to run
printClassStudent(students_per_course)

printStudentClass(courses_per_student)

calc_mean(students_per_course)
calc_median(students_per_course)

make_hist(students_per_course)
make_boxplot(students_per_course)

makeBoxplotInteractions(courses_per_student, students_per_course)

makeHistogramInteractions(courses_per_student, students_per_course)
