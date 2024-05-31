''' 
Code Description
This code is to create Rectangle Pattern using Python language

Creator: Aakash Sharma
'''

#CODE 1
length = int(input("enter the length of rectangle: "))
breadth = int(input("enter the breadth of rectangle: "))
for i in range(length):
  print("* " * breadth)
'''
EXPECTED OUTPUT
enter the length of rectangle:  5
enter the breadth of rectangle: 4
* * * * 
* * * * 
* * * * 
* * * * 
* * * * 
'''

#CODE 2
length = int(input("enter the length of rectangle: "))
breadth = int(input("enter the breadth of rectangle: "))
for i in range(length):
  for j in range(breadth):
    print("* ",end = "")
  print()
  
'''
EXPECTED OUTPUT
enter the length of rectangle:  5
enter the breadth of rectangle: 4
* * * * 
* * * * 
* * * * 
* * * * 
* * * * 
'''
