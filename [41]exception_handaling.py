try:
    age = int (input("age  = "))
except ValueError:
    print("You did't value age ")
else:
    print(" no exception no where")
print("excution continue")