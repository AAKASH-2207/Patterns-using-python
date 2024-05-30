''' 
Code Description
This code is to create Hollow Square Pattern using Python language

Creator: Aakash Sharma
'''

size = int(input("enter the length of each side: "))
for i in range(size):
  for j in range(size):
    if i == 0 or j == 0 or j == size-1 or i == size-1:
      print("* ",end="")
    else: print("  ", end = "")
  print()

'''
EXPECTED OUTPUT
enter the length of each side: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
