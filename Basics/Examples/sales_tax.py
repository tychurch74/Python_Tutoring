
#MA sales tax formatted as a decimal
sales_tax = .0625

#Get sale price from the user and convert the input from a string into a decimal value
sale_price = input("Input sale amount: ")
sale_price = float(sale_price)

#Calculate how much tax is added 
added_tax = sales_tax * sale_price

#Calculate final total and print to terminal
total = added_tax + sale_price
print(f"Total price = ${total}")