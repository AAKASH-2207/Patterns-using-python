'''

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
