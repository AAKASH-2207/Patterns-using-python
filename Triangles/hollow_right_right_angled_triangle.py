''' 
Code Description
This code is to create a Empty Right sided Right angled Triangle using Python language

Creator: Aakash Sharma
'''
size = int(input("enter the size of the triangle: "))
for i in range(size+1):
  for j in range(size-i):
    if(j==0 or j==size-i-1 or i == 0):
      print("* ",end="")
    else:
      print("  ",end ="")
  print()

'''
EXPECTED OUTPUT
enter the size of the triangle: 5
* * * * * 
*     * 
*   * 
* * 
* 
'''
