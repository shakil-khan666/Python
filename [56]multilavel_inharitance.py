class Empolyee:
    def greet(self):
        print("good worker")
        
class person:
    def greet(self):
        print("good man")

class Manager(Empolyee,person):
    pass

manager = Manager()

manager.greet()

