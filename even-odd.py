print("================ Even Odd =========================")

number = int(input("enter a number: "))

if number > 0:

    if number % 2 == 0:
        print("The number is even and positive")
    elif number % 2 != 0:
        print("The number is odd and positive")

    else:
        print("The number is not even")
elif number < 0:

    if number % 2 == 0:
        print("The number is even and negative")
    elif number % 2 != 0:
        print("The number is odd and negative")

else:
    print("the number is zero")