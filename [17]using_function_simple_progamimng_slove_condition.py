 def shakil(input):
    if input%3==0:
        return "fezz"
    elif input%5==0:
        return "buzz"
    elif (input%3==0) and (input%5==0):
        return "fezz buzz"
    else:
        return input
    

print(shakil(7))