''' 
Code Description
This code is to create a Inverted Right angled Triangle using Python language

Creator: Aakash Sharma
'''

#CODE 1 
size = int(input("enter the size of triangle: "))
for i in range(size):
  print("  " * (i) + "* " * (size-i))
'''
EXPECTED OUTPUT
enter the size of triangle: 5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

#CODE 2
size = int(input("enter the size of triangle: "))
for i in range(0, size):
  print("  "*i,end ="")
  for j in range(size, i, -1):
    print("* ",end = "")
  print()

'''
EXPECTED OUTPUT
enter the size of triangle: 5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''
