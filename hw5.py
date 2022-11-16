# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 
def safe_subtract(a,b):
    try:
        return a-b
    except TypeError as e1:
        return None
    except Exception as e:
        print(e)

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

from datetime import date

# EAFP

def retrieve_age_eafp(person):
    
    try:
        return date.today().year - person['birth']
    except KeyError:
        print("Some keys are missing")

# LBYL

def retrieve_age_lbyl(person):
    
    if 'birth' in person:
        return date.today().year - person['birth']
    else:
        print("Some keys are missing")
        
# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double
print(total_double_sum)
#considering that the objective is to get the sum of the doubled elements, 
# the iterated value that is to be cumulatively added to the sum should be the double and not the element itself

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    if len(strings)==0:
        strings+=string
    else:
        strings = strings+"_"+string
print(strings)
#Intended string concatenation does not happen as string is added to itself.
# The string should be added to the original 'strings' variable
#also added an if else condition to recognize start of string

### (c) Careful!
j=10
while j < 10:
   j += 1
print(j)
#infinite loop due to incorrect constraint in the while loop, corrected to have an end/base condition

### (d)
productory = 1
for elem in [1, 5, 25]:
    productory =productory* elem
print(productory)
#product should be taken initialized to 1, or end result will be 0


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(list_string):
    return sum(map(lambda x: x.count('Simba'), list_string))

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# HINT: You can use geopy.distance in order to compute the distance
#
from geopy import distance

def compute_distance(latlong_list:list)->list:
    dist=[]
    for i in latlong_list:
        calc=distance.distance(i[0],i[1]).km
        dist.append(calc)
    return dist


#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

from collections.abc import Iterable

 
def sum_general_int_list(int_list):
    total = 0
    
    for i in int_list:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            total += sum_general_int_list(i)
        else:
            total += i
    
    return total
