n = input("number of columns: ")

while(n.isnumeric() == False or int(n) == False):
  print("Please Derrick chose a valid number of rows :D")
  n = input("number of columns: ")
  
n = int(n)
   
def printTriangle(span, i):
  for j in range((span) - i):
      print(" ", end="")
  
  for k in range(i + (i + 1)):
      print("*", end="")

print("\n ================================ First Pattern =========================== \n")

for i in range(n):
  printTriangle(n, i)
      
  print()
  
  
print("\n ================================ Second Pattern =========================== \n")
  
for i in range(n):
  
  for y in range((n-i)):
    print("*", end="")
  
  for t in range(i + (i -1)):  
    print(" ", end="")
    
  print()
  
  
print("\n ================================ Third Pattern =========================== \n")
 
mid = n // 2 

ifOdd: int

if(n % 2 == 0): 
  ifOdd = 0
else:
  ifOdd = 1


for i in range(mid + ifOdd): 
  for r in range(i+1):
    print('*', end='')
  
  print()
    
for i in range(mid, 0, -1):
    for k in range(i):
      print('*', end='')
      
    print()

print("\n ================================ Fourth Pattern =========================== \n")

for i in range(mid, 0 ,-1):
  printTriangle(mid, i)
  print()
  
for i in range(mid + ifOdd):
  printTriangle(mid, i)
  print()
  

print("\n ================================ Fifth Pattern =========================== \n")

for i in range(mid+ifOdd):
  printTriangle((mid), i)
  print()
  

for i in range(mid, 0, -1):
  printTriangle(mid, i-1)
  print()

