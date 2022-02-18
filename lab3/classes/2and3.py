class Shape: 
    def __init__ (self): 
        pass 
     
    def area(self): 
        return 0 
 
class Square(Shape): 
    def __init__ (self, length): 
        self.length = length 
     
    def area(self): 
        return self.length**2 
 
class Rectangle(Shape): 
    def __init__ (self, length, width): 
        self.length = length 
        self.width = width 
     
    def area(self): 
        return self.length*self.width 
         
S1 = Square(int(input())) 
Sh1 = Shape() 
R1 = Rectangle(int(input()), int(input())) 
print(Sh1.area()) 
print(S1.area()) 
print(R1.area())
