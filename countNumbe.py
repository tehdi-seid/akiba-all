print("================== count numebr==========================")

posetive_number=int(input("Enter a possetive number: "))
odd_counter=0
even_counter=0
sum=0
if posetive_number > 0:
    for number in range(posetive_number):
        # print(number)
        if (number+1) % 2==0:
            even_counter+=1
        else:
            odd_counter+=1
            
        sum+=number
        
    print(f"The number of even numbers is {even_counter}")
    print(f"The number of odd numbers is {odd_counter}")
    print(f"The total sum of the number is {sum}")
        
else:
    print("please enter a posetive number and try again!")
    
    
print("============================================================")