def student_info(name, course="Computer Engineering", *args, **kwargs):
    print("Name:", name)
    print("Course:", course)
    print("Other details:", args)
    print("Extra info:", kwargs)
    print()

# 1. Positional arguments
student_info("Amosi", "DSAI")

# 2. Keyword arguments
student_info(name="Amosi", course="DSAI")

# 3. Default argument
student_info("Anderson")

# 4. *args and **kwargs
student_info("Amosi", "DSAI", "Year 2", "ARDHI", age=22, city="Dar es Salaam")
