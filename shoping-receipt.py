print("========== # Ethiopian Shopping Receipt # =============\n")

name=input("Enter your name: ").title()
product_name=input("Enter product name plese: ").title()
price=int(input("Enter price(ETB): "))
quantity=int(input("Enter quantity: "))

print("\n============================================")
print("                  RECEIPT                   ")
print("============================================\n")

print("Product,", "Total price", "quantity", sep="       ")

toatal_price=quantity*price

print("--------------------------------------------")
print(product_name, f"{toatal_price} ETB", quantity, sep="                ")