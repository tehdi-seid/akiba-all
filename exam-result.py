print("================Exam Result Report=========================")

name = input("Enter the name of the student: ")
python=float(input("Enter python score: "))
english=float(input("Enter english score: "))
math=float(input("Enter mathematics score: "))

average = (python+english+math)/3

print("===========================================================")
print("                     Student result                        ")
print("===========================================================")

print("Student name: ",name)
print("pyhton: ",python)
print("English: ",english)
print("Mathematics: ",math)
print("\n-----------------------------------------------------------")

print("Average:", round(average, 2))
print("===========================================================")
