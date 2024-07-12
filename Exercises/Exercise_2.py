#Ask User to input 3 numbers and you have to print Average  of three numbers using string Formatting

num1,num2,num3 =input("Add 3 numbers Seperated by Comma").split(",")

avg =(int(num1)+int(num2)+int(num3))/3

print(f"Entered {num1} {num2} {num3}'s Average is {avg} ")