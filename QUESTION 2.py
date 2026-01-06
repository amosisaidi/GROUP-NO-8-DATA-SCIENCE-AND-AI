subtotal = float(input("Enter the subtotal: "))
rate = float(input("Enter the gratuity rate without percent sign: "))

gratuity = subtotal * rate / 100
total = subtotal + gratuity

print("The gratuity is", round(gratuity, 2), "and total is", round(total, 2))
 