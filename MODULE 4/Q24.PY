# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class circle:
    def __init__(self):                           # CONSTRUCTOR IN RADIUS
        self.radius=float(input("enter radius:"))      # REDIUS INPUTR TAKEN 
        self.π=3.14
    def area(self):                            # METHOD OF AREA
        print(f"AREA OF CIRCLE IS {self.π*self.radius*self.radius}")    
    def perimeter(self):                            # METHOD OF PERIMETER
        print(f"PERIMETER OF CIRCLE IS {2*self.π*self.radius:.2f}")      
p1=circle()                              # CREATE OBJECT
p1.area()                                # CALLING AREA  METHOD
p1.perimeter()                       # CALLING PERIMETER METHOD



π=14
print(π)