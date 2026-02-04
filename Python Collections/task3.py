languages = {"Python", "Java", "C++", "JavaScript", "Go"}
accents={"british","english","swahili"}
#add items in the sets 
languages.add("SQL")
print(languages)
print()
#remove items from the set
languages.remove("Java")
print(languages)
print()
#discard items from set
languages.discard("R")
print(languages)
print()
#union of sets
print(languages|accents)
print()
#intersection
print(languages&accents)
print()
#differences
print(languages-accents)
print()
