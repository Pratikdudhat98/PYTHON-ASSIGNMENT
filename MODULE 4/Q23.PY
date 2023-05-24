# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 
class rectangle:
    def _init_(self):        # CREATE CONSTRUCTOR
        self.length
        self.width
    def area(self):         # CREATE FUNCTION FOR INPUT
        self.length=float(input("enter length:"))      # INPUT LENGTH
        self.width=float(input("enter width:"))         # INPUT WIDTH
    def show_area(self): # CREATE FUNCTION FOR PRINT
        print(f"AREA OF RACTANGLE IS {self.length*self.width:.2f}")  # PRINT AREA
s1=rectangle()             # OBJECT CREATE
s1.area()
s1.show_area()               