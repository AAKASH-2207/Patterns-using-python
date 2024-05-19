''' 
Code Description
This code is to create a Inverse Hollow Pyramid using Python language

Creator: Aakash Sharma
'''
size = int(input("enter the size of the triangle: "))
for i in range(size+1):
  for k in range(i):
    print(" ",end="")
  for j in range(size-i,-1,-1):
    if(j==size-i or j==0 or i == 0):
      print("* ",end="")
    else:
      print("  ",end ="")
  print()

'''
EXPECTED OUTPUT
enter the size of the triangle: 5
* * * * * * 
 *       * 
  *     * 
   *   * 
    * * 
     * 
'''
