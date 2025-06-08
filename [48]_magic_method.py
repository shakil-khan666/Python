class Add:
    def __init__(self,x,y):
        self.x = x
        self.y = y
      

    def forward(self) :
         return self.x+self.y
         
         
point = Add(1,2)

point.forward()
        