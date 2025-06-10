#Below 25 – F, 25 to 44 – E, 45 to 49 – D, 50 to 59 – C, 60 to 79 – B, 80 to 89 - A, Above 90 - A+
a = int(input("enter the number of a : "))

if a<25:
    print("F")
elif a>25 or a<=44:
    print("E")
elif a>=45 or a<=49 : 
    print("D")
elif a>=50 or a<=59 :
    print("C")
elif a>=60 or a<=79 :
    print("B")
elif a>=80 or a<=89 :
    print("A")
elif a>=90 or a<=100 :
    print("D")
