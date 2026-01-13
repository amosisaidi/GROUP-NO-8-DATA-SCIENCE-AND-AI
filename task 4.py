string_1=str(input("Enter First string;"))
string_2=str(input("Enter Second String;"))

if string_1 == string_2:
    print("The strings are equal")
else:
    print("The strings are not equal")
    
print()

if len(string_1)>len(string_2):
    print("First strinng is longer than second string")
else:
    print("Second strinng is longer than first string")
