#Cliff Jorgensen

print()
#variables for retail cost and discount
app_cost = 99
discount = 0
#prompts user to enter license quantity 
license_num = int(input("Enter quantity of licenses purchased: "))
print()
#outputs error message if nothing is purchased
if license_num <= 0:
    print("Error")
#calculates price for 1-9 purchased, no discount applied
elif license_num >= 1 and license_num <= 9:
    app_cost = license_num * app_cost 
    print("No Discount Applied")
    print()
    print("Discount = ", discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)
    
#applies 10% discount for 10-19 purchased
elif license_num >= 10 and license_num <= 19:
    discount = license_num * app_cost * 0.1
    app_cost = license_num * app_cost - discount
    print("10% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)
    
#applies 15% discount for 20-29 purchased
elif license_num >= 20 and license_num <= 29:
    discount = license_num * app_cost * 0.15
    app_cost = license_num * app_cost - discount
    print("15% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)

#applies 20% discount for 30-39 purchased    
elif license_num >= 30 and license_num <= 39:
    discount = license_num * app_cost * 0.20
    app_cost = license_num * app_cost - discount
    print("20% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)

#applies 25% discount for 40-49 purchased
elif license_num >= 40 and license_num <= 49:
    discount = license_num * app_cost * 0.25
    app_cost = license_num * app_cost - discount
    print("25% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)
    
#applies 30% discount for 50-59 purchased
elif license_num >= 50 and license_num <= 59:
    discount = license_num * app_cost * 0.30
    app_cost = license_num * app_cost - discount
    print("30% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)

#applies 35% discount for 60-69 purchased
elif license_num >= 60 and license_num <= 69:
    discount = license_num * app_cost * 0.35
    app_cost = license_num * app_cost - discount
    print("35% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)

#applies 40% discount for 70 or more purchased
else:
    discount = license_num * app_cost * 0.40
    app_cost = license_num * app_cost - discount
    print("40% discount applied")
    print()
    print("Discount = $", "%.2f" % discount)
    print()
    print("Total cost = $", "%.2f" % app_cost)


