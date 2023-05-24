# Write a Python program to calculate the area of a trapezoid 
def trapezoid(a,b,c):
    return (a+b)/2*c      # CALCULATE AREA
n1=float(input("enter base:"))                   # INPUT BASE
n2=float(input("enter base:")) 
n3=float(input("enter height:"))         # INPUT HEIGHT
print(f"AREA OF TRAPEZOID IS {trapezoid(n1,n2,n3)}")    
