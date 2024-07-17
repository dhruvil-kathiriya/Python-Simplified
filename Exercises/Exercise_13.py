### break Statement
while True:
    
    n = int(input('Enter a number'))
    
    if n > 0:
        print('Positive')
    elif n < 0:
        print('Negative')
    else:
        break;
    
    
### Continue Statement

count = 0 

while count < 10:
    n = int(input('Enter a number'))
    
    if n % 3 == 0:
        continue
    print(n)
    count += 1
    
print(count)
    
### Pass Statement

count = 0 

while count < 10:
    n = int(input('Enter a number'))
    
    if n % 3 == 0:
        pass
    else :
        print(n)
    count += 1
    
print(count)