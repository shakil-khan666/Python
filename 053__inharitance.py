class Animal:
     def eat(self):
         print("eat")
     
class Minimal(Animal):
     def water(self):
        print("water")
    
class Fish(Animal):
     def swim(self):
        print("swim")
    
m = Minimal()
m.eat()
m.water()
