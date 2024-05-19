''' 
Code Description
This code is to create a Hollow Pyramid using Python language

Creator: Aakash Sharma
'''
size = int(input("enter the size of the triangle: "))
for i in range(size+1):
  for k in range(size-i):
    print(" ",end="")
  for j in range(i+1):
    if(j==0 or j==i or i == size):
      print("* ",end="")
    else:
      print("  ",end ="")
  print()
'''
EXPECTED OUTPUT
enter the size of the triangle: 5
     * 
    * * 
   *   * 
  *     * 
 *       * 
* * * * * * 
'''
