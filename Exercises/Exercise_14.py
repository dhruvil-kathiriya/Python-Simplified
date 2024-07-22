msg = 'hello'

for x in msg:
    print(x)
    
    
for i in range(0,10,2):
    print(i)
    
    
### Display Multiplication table for given number

n = int(input("Enter a value"))

for i in range(1,11):
    print(f'{n} x {i} = {n*i}')


### Find the Factorial of a given number

n = int(input('Enter a Number : '))
fact = 1 

for count in range(1,n+1):
    fact = fact * count
print('Factorail of',n,'is',fact)