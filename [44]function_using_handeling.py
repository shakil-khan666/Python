def calculeting(age):
    if age <=0:
        raise ValueError ("code error sorry")
    return 10/age

try:
   calculeting(10)
except ValueError as error :
    print(error)