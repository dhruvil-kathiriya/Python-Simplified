### Calculate discounted amount

# amount<= 1000 10%
# 1000 < amount <=5000 20%
# 5000 < amount <=10000 30%
# 10000 < amount  50%

amount = float(input("Enter Amount : "))

if amount <= 1000:
    discount = amount * 10/100
elif amount > 1000 and amount <= 5000:
    discount = amount * 20/100
elif amount > 5000 and amount <= 10000:
    discount = amount * 30/100
else:
    discount = amount * 50/100
    
pay = amount - discount
print(f'You Final Payment is {pay}')
     
  
### Take a day Number and print day name                 

day = int(input('Enter day number from week'))

if day == 1:
    print('Sunday')
elif day == 2:
    print('Monday')
elif day == 3:
    print('Tuesday')
elif day == 4:
    print('Wednesday')
elif day == 5:
    print('Thursday')
elif day == 6:
    print('Friday')
elif day == 7:
    print('Saturday')
else:
    print('Invalid Day Number')
    
