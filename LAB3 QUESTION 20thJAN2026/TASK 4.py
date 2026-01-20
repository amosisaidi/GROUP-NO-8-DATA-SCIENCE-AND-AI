def change_number(x):
    x = 100

def change_list(lst):
    lst[0] = 999


print("Integer example")
num = 10
print("Before:", num)
change_number(num)
print("After:", num)

print("\n")

print("List example")
my_list = [1, 2, 3]
print("Before:", my_list)
change_list(my_list)
print("After:", my_list)
