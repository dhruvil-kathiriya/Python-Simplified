### Print n terms of AP(Arithmatic Progression) Series
# -- Difference between two index should be same throughout whole series
# -- Example : 5,7,9,11,13 --  starting a = 5 ,Difference is 2, terms(total elements) n = 5

a = int(input('Enter initial term : '))
d = int(input("Enter common Difference : "))
n = int(input('Enter number of terms'))

for t in range(a, a +  n * d, d):
    print(t)
    
### Print n terms of Fibonacci series

n = int(input('Enter number of terms : '))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
    
    