# Grocery Store Billing System
# Case Study-1
# Subject: Python for Engineers (AI102P)

# Taking input for 3 items from the user
a = int(input("Enter price of item 1: "))
b = int(input("Enter price of item 2: "))
c = int(input("Enter price of item 3: "))

# Calculating total amount
total = a + b + c

# Checking if total is greater than 50 to apply discount
if total > 50:
    discount = total * 0.10   # 10% discount
    final_amount = total - discount
    
    print("Original Total:", total)
    print("Discount Applied (10%):", discount)
    print("Final Payable Amount:", final_amount)

else:
    # If total is 50 or less, no discount
    print("Original Total:", total)
    print("No Discount Applied")
    print("Final Payable Amount:", total)
