''' 
Code Description
This code is to create a left sided Right angled Triangle using Python language

Creator: Aakash Sharma
'''

no_of_rows = int(input("enter the size of the Triangle: "))
for rows in range(0, no_of_rows): 											# First for loop for the no. of rows to be in the triangle
  for columns in range(0, rows+1):  												  # second loop for the steps or column length 
    print("* ",end="") 				 			 												# printing the steps
  print("") 																								# printing the next line

'''
expected Output:
enter the size of the Triangle: 5
* 
* * 
* * * 
* * * * 
* * * * * 
'''

#CODE 2
size = int(input("enter the size of triangle: "))
for i in range(size):
  print("* " * (i+1))
'''
EXPECTED OUTPUT
enter the size of triangle: 5
* 
* * 
* * * 
* * * * 
* * * * * 
'''
