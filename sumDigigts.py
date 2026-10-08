print("================ sum of digits===================")

digits = input("enter a number: ")

accomolator = 0

repeater = 0

while repeater < len(digits):
    accomolator += int(digits[repeater])
    repeater+=1
    
# for digit in digits:
#     accomolator+=int(digit)
    
print(f"The sum of the digit is: {accomolator}")

print("==================================================")