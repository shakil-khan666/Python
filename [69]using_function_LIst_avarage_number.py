def add_number(numbers):
    result = 0
    for i in numbers:
        result = result+i
    print( "result = ",result)
    
    if numbers ==0:
        print("empty List")
    avarage = result/len(numbers)
    
    print("avarage = ",avarage)

number_list = [int(x)for x in input("enter the separeted number ").split()]
add_number(number_list)

                                    
