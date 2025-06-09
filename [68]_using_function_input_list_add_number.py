def add_numbers(numbers):
    result =0 
    for i in numbers:
        result = result+i
        

    print(result)
   
    
n=[int(x) for x in input("Enter numbers separated by space: ").split()]
add_numbers(n)