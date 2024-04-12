''' 
Code Description
This code is to create a right sided Right angled Triangle using Python language

Creator: Aakash Sharma
'''

height = int(input("enter the size of the pyramid: "))

# CODE 1

for i in range(1,height+1):
  print("  "*(height - i) + " *" * i)
  # SMALLER TIME COMPLEXITY

# CODE 2

for i in range(1,height+1):
  for j in range(height-i):
    print("  ",end="")
  for k in range(i):
    print("* ",end="")
  print("")

'''
EXPECTED OUTPUT:

enter the size of the pyramid: 5
         *
       * *
     * * *
   * * * *
 * * * * *
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
  
