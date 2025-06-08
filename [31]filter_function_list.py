items = [
    
    ("shakil",10),
    ("rahim",20),
    ("karim",5)
    
    ]

x = list( filter(lambda items:items[1]>=10,items))

print(x)