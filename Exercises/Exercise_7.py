### Check if number is positive or Negative 
a = int(input('Enter a number'))

if a < 0:
    print("Negative")
else:
    print("Positive")
    
    
### Find the Difference between two Numbers

no1 = int(input('Enter a number '))
no2 = int(input('Enter a number '))

if no1 - no2 >= 0:
    print(no1 - no2)
else:
    print(no2 - no1)
    
### Check if a number is Odd or Even

a = int(input("Enter a number"))

if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


### Check for Age eligibility for casting a vote

age = int(input('Enter your age :'))

if age >= 18:
    print('You are Eligible for Voting')
else:
    print('Ypu are not eligible for voting')