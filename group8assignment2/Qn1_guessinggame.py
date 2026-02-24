win = 1000
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    attempts += 1
    remaining = max_attempts - attempts
    
    try:
        n_guess = int(input("enter number,"))
        
        if n_guess == win:
            print("Win")
            break 
        else:
            if remaining > 0:
                print(f"Wrong..! Try again,")
            else:
                print("Wrong..! Times up")
                
    except:
      print(f"Invalid input. {remaining} attempts left.")

        
