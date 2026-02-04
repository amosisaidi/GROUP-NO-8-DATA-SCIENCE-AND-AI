students = {
"Alice": 78,
"Bob": 65,
"Carol": 82,
"David": 59
}

#accesing value from key
print("Accesing Value from Key")
print("The age of Alice is: ",students["Alice"])
print()
#getting items from a dictionery
print("Getting items from a Dictionery")
print("The age of bob is: ",students.get("Bob"))
print()
#get dictionery keys
print("Get Dictionery Keys")
print("The keys in Dictionary are: ", students.keys())
print()
#get values of the dictionery
print("Get Values of the Dictionery")
print("The values in Dictionary",students.values())
print()
#get items from the dictionery
print("get items from dictionery")
print("the items from dictionery,",students.items())
print()
#updating the dictionery
students.update({"Alice":15,"Carol":20})
print("updated students dictionery:\n",students)
#remove random item from dictionery
print("random item removed from dictionery:\n",students.pop("Alice"))