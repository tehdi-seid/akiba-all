print("================== Number guesing  game =========================")

secret_num = 12
attempt_accomolator=1
available_attempt = 5
while available_attempt >= 1:
    print(f"you only have {available_attempt} attempts")
    number=int(input("Enter a number: "))
    if number==secret_num:
        print(f"You guesed the number by {attempt_accomolator} attempts")
        break
    elif number > secret_num:
        print("It is too high")
        attempt_accomolator+=1
        available_attempt-=1
    elif number < secret_num:
        print("it is too low")
        attempt_accomolator+=1
        available_attempt-=1
        
if available_attempt ==0:
    print("Game Over, you have finished your attempt")     
print("===================================================================")