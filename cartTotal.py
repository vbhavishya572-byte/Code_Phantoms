# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



headPhone = 999 # parenthises are not required
smartWatch = 1599 # parenthises are not required
PS5 = 1299 #parenthises are not required
iPad = 599# parenthises are not required


productName = str(input("Enter Product Name: ")) # type was not mentioned 


quantity = int(input("Enter the Quantity of the Product: ")) # type was not mentioned


if productName == "headPhone":
    totalPrice = headPhone * quantity

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity  # in smartwatch W is small we corrected it

elif productName == "PS5":
    totalPrice = PS5 * quantity

elif productName == "iPad": # in ipad P is small
    totalPrice = iPad * quantity


print(f"Total Amount To Be Paid: {totalPrice}");