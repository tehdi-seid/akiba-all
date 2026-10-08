print("============== PRIME NUMBER CHECKER ===============\n")

num=int(input("Enter a number: "))

counter = 1

while True:
    if num==0 or num==1 or counter > 2:
        print("your number is not prime")
        break
    elif num == 2:
        print("your number is prime")
        break
    else:
        counter +=1
        
print("===========================================================")

        