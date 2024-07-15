### Check if a student has passed or failed, by taking marks in 3 subjects 

math = int(input("Enter Math marks "))
phy = int(input("Enter Physics marks "))
eng = int(input("Enter English marks "))

if math >= 45 and phy >= 45 and eng >= 45:
    print("Passed")
else:
    print('Failed')
    
    
### Check if a person has Access or not 

username = input('Enter your username')

if username == 'john' or username == 'smith':
    print('Authorized')
else:
    print('Unauthorized')
    
    
### Check if a given lowercase character is vowel or consonant

char = input('Enter lowercase Character')

if char == 'a' or char == 'e' or char == "i" or char == 'o' or char == 'u':
    print('vowel')     
else:
    print('Consonent')