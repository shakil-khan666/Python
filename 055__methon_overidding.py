class Animal:
    def __init__(self):
        
        self.age = 1
   
    def eat(self):
        print("eat")

class Fish(Animal):
    def swim(self):
        print("swim")
    def __init__(self):
       self.time = 2
       super().__init__()

class Vagitable(Animal):
    def potato(self):
        print("potato")
  
     

f = Fish()
f.eat()
print(f.age)
print(f.time)
