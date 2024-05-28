''' 
Code Description
This code is to create Square Pattern using Python language

Creator: Aakash Sharma
'''

#CODE 1
size = int(input("enter the length of each side: "))
for i in range(size):
  for j in range(size):
    print("* ",end="")
  print()

'''
EXPECTED OUTPUT
enter the length of each side: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
#CODE 2
size = int(input("enter the length of each side: "))
for i in range(size):
  print("* " * size)
  
'''
EXPECTED OUTPUT
enter the length of each side: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
