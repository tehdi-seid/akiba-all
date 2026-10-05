print("================BMI Health Information=========================")

name = input("Enter enter your name: ")
weight=float(input("Enter weght(Kg): "))
height=float(input("Enter height(M): "))


print(height**2)

bmi=weight/(height**2)

print("===========================================================")
print("                       BMI REPORT                          ")
print("===========================================================")

print("Student name: ",name)
print("Weight: ",weight)
print("Height: ",height)
print("\nBMI:", round(bmi, 2))
print("===========================================================")
