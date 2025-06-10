def number_sum(L):
    even_sum = 0
    odd_sum = 0
    for i in L:
        if i%2==0:
            even_sum = even_sum+i
           
        else:
            odd_sum = odd_sum +i
    print( even_sum)
    print( odd_sum )
        
            

L=[1,2,4,5,6,7]
number_sum(L)