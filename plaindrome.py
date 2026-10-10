print("===================plaindrome checker=======================\n")

value=input("enter any word: ")
# print(value.lower())



if value.lower()== value.lower()[::-1]:
    print("the word is plaindrome")
    
else:
    print("the word is not palindrome")


print("===========================================================")
