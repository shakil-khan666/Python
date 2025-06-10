class Point :
    
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @classmethod
    def zero(cls):
        return cls
        
    def draw(self):
        print(f"Point({self.x} {self.y})")
Point.defult_color =" green"        

point = Point(0,0)
point.draw()

