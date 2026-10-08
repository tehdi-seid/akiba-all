print("================ fizzbezz ===================")


start_num = int(input("Enter the starting num: "))
end_num = int(input("Enter the ending num: "))


print("=============================================")
if start_num > end_num:
    print("The starting number must be greater than the ending number")
    
else:
    
    while start_num <= end_num:
        if start_num % 3==0 and start_num % 5==0:
            print("FizzBuzz")
            start_num+=1
        elif start_num % 3==0:
            print("Fizz") 
            start_num+=1
        elif start_num % 5==0:
            print("Buzz")
            start_num+=1
        else:
            print(start_num)
            start_num+=1
            
            
print("=============================================")
