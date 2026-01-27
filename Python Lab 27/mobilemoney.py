n = input("Dial *150*01# :")
while n != "*150*01#":
    print("Dialed wrong number")
    n = input("Dial *150*01# :")
    
def send_money():
    print("SEND MONEY")
    print()
    print(
        "1.To Same Network\n"
        "2.To Other Network\n"
    )
    
    s = int(input("Enter Choice: "))
    
    if s == 1:
        print("Enter Choice in form of 0712345678")
        pn = int(input("Enter Phone Number: "))
        am = int(input("Enter Amount: "))
    elif s == 2:
        net = input("Enter Network name: ")
        print("Enter Choice in form of 0712345678")
        pn = int(input("Enter Phone Number: "))
        am = int(input("Enter Amount"))
    else:
        print("Invalid input")
        return pn, net, am# Exit the function if input is invalid
    
    print("successful")

print()
print("WELCOME TO MIXX BY YASS USER MENU")
print()

print(
    "1.Send Money\n"
    "2.Buy Airtime\n"
    "3.Pay Bills\n"
    "4.Check Balance\n"
    "5.Exit"
    )

choice = int(input("Enter choice: "))

if choice == 1:
    send_money()
else:
    print("No")
