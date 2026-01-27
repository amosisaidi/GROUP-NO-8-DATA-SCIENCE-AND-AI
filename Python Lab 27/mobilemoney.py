n = input("Dial *150*01# :")
while n!="*150*01#":
    print("Dialed wrong number")
    n = input("Dial *150*01# :")
    
def send_money():
    print("SEND MONEY")
    print()
    print(
        "1.To Same Setwork\n"
        "2.To Other Network\n"
        )
    
    s = int(input("Enter Choice: "))
    
    if s==1:
        print("Enter Choice in form of 0712345678")
        pn = int(input("Enter Phone Number: "))
    elif s==2:
        net = input("Enetr Network name: ")
        print("Enter Choice in form of 0712345678")
        pn = int(input("Enter Phone Number: "))
    else:
        print("Invalid input")
    print("succesfull")


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
if s==1:
    send_money()
else:
    print(no)
