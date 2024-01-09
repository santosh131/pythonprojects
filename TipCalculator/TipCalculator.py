total_bill_amount = float(input("Please enter total Bill amount "))
no_of_users = int(input("Please enter number of Users to split the bill "))
tip_percent = int(input("Please enter the Percentage of tip to applied for the bill "))
tip_amount= (total_bill_amount * tip_percent) / 100
final_amount = (total_bill_amount + tip_amount)/ no_of_users
final_amount ="{:.2f}".format(final_amount)
print(f"Total bill for each user is ${final_amount}")

