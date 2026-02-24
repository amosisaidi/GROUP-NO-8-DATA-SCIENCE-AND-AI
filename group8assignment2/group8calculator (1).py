def Addition():
    print("\nAddition: X + Y")
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    a = x + y
    print(f"\t{x} + {y} = {a}\n")
    return a

def Subtraction():
    print("\nSubtraction: X - Y")
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    a = x - y  
    print(f"\t{x} - {y} = {a}\n")
    return a

print("Group 8 CALCULATOR \n")
while True:
    try:
        print("Pick Selection")
        print("1.) Addition")
        print("2.) Subtraction")
        print("3.) Quit")
 
        se = input("Select (1, 2  or 3): ").lower().strip()
        
        if se == "1":
            Addition()
        elif se == "2":
            Subtraction()
        elif se == "3":
            break
        else:
            print("Invalid input\n")
   
            
    except ValueError:
        print("Error: Please enter numbers only!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

print("Program Terminated")
