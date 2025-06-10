class TagCloud:
    def __init__(self):
        self.tags = {} 
        
    def add(self,tag):
        self .tags[tag]=self.tags.get(tag,0)+1

cloud = TagCloud()

cloud.add("pyhton")
cloud.add("shakil")
cloud.add("Pyhton")
cloud.add("shakil")
cloud.add("Pyhton")

print(cloud.tags)

        
        
        
        
