print("================BMI Health Information=========================")

name = input("Enter enter your Name: ")
weight=float(input("Enter Weght(Kg): "))
height=float(input("Enter Height(M): "))


print(height**2)

bmi=weight/(height**2)

print("===========================================================")
print("                       BMI REPORTs                          ")
print("===========================================================")

print("Student name: ",name)
print("Weight: ",weight)
print("Height: ",height)
print("\nBMI:", round(bmi, 2))
print("===========================================================")
