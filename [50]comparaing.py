class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __gt__(self,other):
        return self.x>other.y and self.y > other .y 

point = Point(1, 2)
other = Point(4, 6)

print(other>point)