
try:
    with open("clening_up_handaling_fopen.py") as file:
        print("file open")
  age = int(input("age  ="))
    
    div = 10/age
except( ValueError,ZeroDivisionError):
    print("You did't value age ")
else:
    print(" no exception no where")
print("excution continue")
 
