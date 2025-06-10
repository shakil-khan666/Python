class TagCloud:
    def __init__(self):
        self.tags = {}
    def add(self,tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0)+1

cloud = TagCloud()

cloud.add("shakil")
cloud.add("Shakil")
cloud.add("shakil")
cloud.add("Shakil")

print(cloud.tags)
        
