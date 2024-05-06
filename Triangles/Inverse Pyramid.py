
''' 
Code Description
This code is to create a Inverse Triangle using Python language

Creator: Aakash Sharma
'''

#CODE 1
height = int(input("enter the height of pyraid: "))
for row in range(height, -1,-1):
    print(" " * (height - row) + "#" * ((row*2)-1))

'''EXPECTED OUTPUT
enter the height of pyramid: 5
#########
 #######
  #####
   ###
    #
    
'''

#CODE 2
for i in range(0,no_of_rows + 1):
  for k in range(0,i):
    print(" ",end="")
  for j in range(no_of_rows-i,0,-1):
    print("* ",end="")
  print("")


'''
EXPECTED OUTPUT
* * * * * 
 * * * * 
  * * * 
   * * 
    *
'''
