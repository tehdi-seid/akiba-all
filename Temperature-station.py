print("========== Temperature Station =============\n")

choice=int(input("Convert To celsius input (1), To  fahrenhiet input(2): "))


match(choice):
    case 1:
        temp=float(input("enter a temperature( in Fahrenhiet): "))
        
        celsius = 5/9*(temp-32)
        
        print(f"\nFahrenhiet: {temp}°F")
        print(f"Celsius: {round(celsius, 2)}°C")
        
    case 2:
        
        temp=float(input("enter a temperature( in Celsiuss): "))

        fahrenheit=(temp*9/5)+32

        print(f"\nCelsius: {temp}°C")
        print(f"Fahrenhiet: {fahrenheit}°F")