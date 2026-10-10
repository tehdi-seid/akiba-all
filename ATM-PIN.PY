print("===================ATM PIN SYSTEM======================")

correct = "1234"
attempt = 3
while attempt >= 0:
    if attempt == 1:
        print("It your last attept")
    else:
        print(f"you have {attempt} attempts")
        
    pin =  input("Enter your pin: ")
    
    if pin!=correct:
        print("Incorrect pin!")
        if attempt==1:
            print("you have finishe your attempts!")
            break
        attempt-=1
    elif pin==correct:
        print("VERIFIED!")
        break
    
print("========================================================")