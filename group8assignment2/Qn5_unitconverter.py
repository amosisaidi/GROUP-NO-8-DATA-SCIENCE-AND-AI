def cm_to_m():
    print("Converting cm to m")
    x = float(input("Enter cm: "))
    y = x/100
    print(f"\t{x} cm is equivalent to {y} m\n")
    return y

def m_to_cm():
    print("Converting m to cm")
    x = float(input("Enter m: "))
    y = x*100
    print(f"\t{x} m is equivalent to {y} cm\n")
    return y

print("Group 8 UNIT CONVERTER\n")
while True:
    try:
        print("Pick Selection")
        print("1.) cm to m")
        print("2.) m to cm")
        print("3.) Quit\n")
 
        se = input("Select (1, 2  or 3): ").lower().strip()
        
        if se == "1":
            cm_to_m()
        elif se == "2":
            m_to_cm()
        elif se == "3":
            break
        else:
            print("Invalid input\n")
   
            
    except ValueError:
        print("Error: Please enter numbers only!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")

print("Program Terminated")
