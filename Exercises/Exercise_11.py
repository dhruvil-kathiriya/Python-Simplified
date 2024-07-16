count = 0 

while count < 10:
    print('hello')
    count += 1

n = int(input('Enter Integer'))

while n > 0 :
    r = n % 10   # Gives Last number from input
    n = n // 10    
    print(r)


### Display Multiplication table for a given number 

n = int(input('Enter a number for Multiplication table'))
a = 1
while a <= 10:
    print(f'{n} X {a} = {a * n}')
    a+=1


### Counting the number of digits in a number

num = int(input('Enter Number '))
count = 0
while num > 0:
    num =  num // 10
    count += 1
    
print(count)


### Find sum of digits in a number 

num = int(input('Enter Number '))
sum = 0
while num > 0:
    r =  num % 10
    num = num // 10
    sum += r
    
print(sum)

### Reversing a number

num = int(input('Enter Number '))
rev = 0
while num > 0:
    r =  num % 10
    num = num // 10
    rev = rev * 10 + r    
    
print(rev)


### Check if a number is a pelindrome 

num = int(input('Enter Number '))
rev = 0
m = num
while num > 0:
    r =  num % 10
    num = num // 10
    rev = rev * 10 + r    
    
if rev == m:
    print('pelindrom')
else:
    print('Not Pelindrome')
    

### find sum of given numbers as input

num_of_nos = int(input('Enter Number'))
sum = 0
count = 0
while count < num_of_nos:
    sum += num_of_nos
    count += 1
