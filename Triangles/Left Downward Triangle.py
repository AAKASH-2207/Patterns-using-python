'''
Code Description
This code is to create a left sided Right angled Triangle using Python language

Creator: Aakash Sharma
'''

#CODE 1
size = int(input("enter the size of Triangle: "))
for row in range(size):
  for coumn in range(size-row):
    print("* ",end="")
  print("")

'''
EXPECTED OUTPUT
enter the size of Triangle: 5
* * * * * 
* * * * 
* * * 
* * 
* 
'''

#CODE2 2
