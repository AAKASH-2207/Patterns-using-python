''' 
Code Description
This code is to create a Pyramid using Python language

Creator: Aakash Sharma
'''
height = int(input("enter the size of Pyramid: "))

#CODE 1:
for row in range(1,height+1):
    print(" " * (height - row) + "#" * ((row*2)-1))

#EXPECTED OUTPUT FOR CODE 1:
'''
enter the size of Pyramid: 5
    *
   ***
  *****
 *******
*********
'''

#CODE 2

for i in range(1,height+1):
  print(" "*(height - i) + "* " * i)

#EXPECTED OUTPUT FOR CODE 1:
'''
enter the size of Pyramid: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''
