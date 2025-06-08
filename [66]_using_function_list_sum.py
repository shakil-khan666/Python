def add_number(numbers):
    result = 0
    for number in numbers:
        result = result+number
    return result

n =[10,20,30,40,50]
result =add_number(n)
print(result)