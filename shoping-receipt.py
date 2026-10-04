print("========== # Ethiopian Shopping Receipt # =============\n")

repitation=2
products=[]
while repitation > 0:
        
    name=input("Enter your name: ").title()
    product_name=input("Enter product name plese: ").title()
    price=int(input("Enter price(ETB): "))
    quantity=int(input("Enter quantity: "))
    
    products.append({
        "name":name,
        "product_name":product_name,
        "price":price,
        "quantity":quantity
    })

    print("------add a second product-----")
    
    repitation-=1

print(products)
print("\n============================================")
print("                  RECEIPT                   ")
print("============================================\n")

print("Product,", "Total price", "quantity", sep="       ")

print("--------------------------------------------")
toatal_price=0
for product in products:
        toatal_price_each=product["quantity"]*product["price"]
        toatal_price+=toatal_price_each
        print(product["product_name"], f"{toatal_price_each} ETB", product["quantity"], sep="                ")
    
print(f"\nTotal price {toatal_price}")

print("Thanks for shoppin")

print("============================================\n")
