correct_number = 6

guess = int(input("Guess a number between 1 and 9: "))

while guess != correct_number:
    if guess >9:
        print("The number is out of range")
    guess = int(input("Wrong guess. Try again: "))

print("Well guessed!")
