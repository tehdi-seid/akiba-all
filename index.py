# name= input("what is your name: ")

# print("hello,",name )

"""
this is a multiple line comment in python

"""

# name=name.strip().title()

# PRINT FUNCTION 

# print("tehdi", name, end="",sep=" ")


# first, last = name.split(" ")

# print("hello", last)

# =============================================================================

"""x=float(input("enter the first num: "))
y=float(input("enter the second num: "))

print(f"{x+y:.2f}")"""

# =============================================================================

# FUNCTION IN PYTHON

# def hello(to="world"):
#     print("hello", to)

# hello()
# acceptor=input("what is your name: ")
# hello(acceptor)
# =============================================================================

# conditinals in python

# number_1=int(input("enter a number: "))
# number_2=int(input("enter another number: "))

# if number_1>number_2:
#     print("the first number is greater than the second number")
    
# elif number_1<number_2:
#     print("the second is greater than the first number ")
    
# else:
#     print("they are equal")

# =============================================================================
# the or operator

# if not number_1 > number_2 or not(number_1 < number_2):
#     print("the first number is equal to the second numbrer")


# def is_even(n):
    # if n%2==0:
    #     return True
    # else:
    #     return False
    
    
    # or
    
    # return True if n%2==0 else False
    
    # or
    
    
    # return n % 2 == 0
    
    
# even_num=int(input("enter a number that you wnat to test the eveness: "))

# print(is_even(even_num))
# =============================================================================

# match in python

# match even_num:
#     case 12:
#         print("it is twelve")
#     case 1:
#         print("this is number one")
#     case _:
#         print("not recognized")        

# =============================================================================

# loops
num=5

while num > 0:
    print("meow")
    num-=1


# we can also do this by using for loop

for _ in range(3):
    print("meow")
    
for i in [1,3,5,5,7,4,343,4,343,43,]:
    print(i)
    
print("meow\n"*3)

def return_posetive():
    
    while True:
        num=int(input("enter sth"))
    
        if num>0:
            print(num)
            return num
    
        print("enter a posetive number")
# =============================================================================

# python dictionary

fam = {
    "tehdi": "seid",
    "seid": "dad",
    "fatima": "mom",
    "muju": "brother",
    
}

for family in fam:
    print(family, fam[family], sep=", ")
    
    
# nested for loop

for _ in range(4):
    for _ in range(4):
        print("#", end="")
        
    print()
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================

