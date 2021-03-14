cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))
if selling_price>cost_price:
    print("The product sold by the profit of RS.",selling_price-cost_price)
else:
    print("The product sold by the loss of RS.",cost_price-selling_price)