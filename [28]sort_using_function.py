items = [
   
   ("product", 10),
   ("product", 9),
   ("product", 8)
    
      ]

def short_item(items):
    return items[1]


items.sort(key=short_item)
print(items)