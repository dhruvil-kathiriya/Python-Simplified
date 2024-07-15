### Check if Marksof subject are within range 0-100

marks = int(input('Enter marks : ')) 

if marks >= 0 and marks <= 100:
    print("Valid")
else:
    print("Invalid")
    
    
### Check if a person is 'Male' or 'Female'

gender = input('enter m for Male and f for female ')

if gender == "m" or gender == "M":
    print("Male")
elif gender == "f" or gender == "F":
    print("Female")
else: 
    print("Invalid Input")


### Check if a person is eligible to work

age = int(input('Enter your age'))

if age >=18 and age <=60:
    print("Eligible to work")
else:
    print("Not Eligible to work")
    