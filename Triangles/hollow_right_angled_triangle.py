''' 
Code Description
This code is to create a Empty left sided Right angled Triangle using Python language

Creator: Aakash Sharma
'''
size = int(input("enter the size of the triangle: "))
for i in range(size+1):
  for j in range(i):
    if(j==0 or j==i-1 or i == size):
      print("* ",end="")
    else:
      print("  ",end ="")
  print()

'''
EXPECTED OUTPUT
enter the size of the triangle: 6
* 
* * 
*   * 
*     * 
*       * 
* * * * * *
'''
