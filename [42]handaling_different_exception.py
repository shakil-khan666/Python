try:
    age = int (input("age  = "))
    
    div = 10/age
except( ValueError,ZeroDivisionError):
    print("You did't value age ")
else:
    print(" no exception no where")
print("excution continue")