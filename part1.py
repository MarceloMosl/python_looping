number = input("Enter the number: ")
n = input("Enter the digit position (from the right): ")

while (number.isnumeric() == False or n.isnumeric() == False or len(number) < int(n) or int(n) <= 0 or int(number) <= 0):
  print("\nPlease use a valid input Mr. Park, your Number and Digit Position should be integers \nAnd the Digit Position should not be higher than the Number's length, Thank you :D\n")
  number = input("Enter the number: ")
  n = input("Enter the digit position (from the right): ")
  
n = int(n)
number = int(number)  

nth_digit = (number // (10 ** (n - 1))) % 10

def ordinal(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

print(f"The {ordinal(n)} digit from the right is: {nth_digit}")
