class Point :
    defult_color = " red"
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"Point({self.x} {self.y})")
Point.defult_color =" green"        

point = Point(1,2)
point.draw()
print(Point.defult_color)

 
point = Point(3,2)
point.draw()
        

print(Point.defult_color)
