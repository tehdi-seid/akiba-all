print("================ laregest of the three number =========================")


num1=float(input("enter the first number: "))
num2=float(input("enter the second number: "))
num3=float(input("enter the third number: "))

if num1 > num2 and num1 > num3:
    print(f"the first({num1}) number is largest")
elif num2 > num1 and num2>num3:
    print(f"the second number({num2}) is the largest")
    
elif num3 > num2 >num1:
    
    print(f"the third number({num3}) is greater")
    
elif num3==num2==num3:
    print("all numbers are equal")
    
elif num3==num2 != num1:
    print(f"the last two number({num2} & {num3}) are equal")
    
elif num3 !=num1 ==num2:
    print(f"the first ({num1}) and the second ({num2}) numbers are equal")
    
elif num3==num1!=num2:
    print("the first and the last numbers are equal")
    
else:
    print("try again")
    
    
