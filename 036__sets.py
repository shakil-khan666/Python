number =  [1,2,3,4,5]

first =  set(number)

print(first)

second = { 2,4,6}

a = first | second
b = first & second
c = first- second
d = first^second

print(a)
print(b)
print(c)
print(d)

if 6 in second:
    print("True")
