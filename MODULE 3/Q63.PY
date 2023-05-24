# Write a Python program to calculate surface volume and area of a cylinder.
def calculation(a,b):
    return 2*3.14*a*b + 2*3.14*a*2       # CALCULATE AREA
def volume(a,b):    
    return 3.14*a*2            # CALCULATE VOLUME

r=float(input("enter radius:"))   #ENTER RADIUS
h=float(input("enter height:"))   #ENTER HEIGHT
c=calculation(r,h)
d=volume(r,h)
print(f"AREA IS {round(c,2)}")    
print(f"VOLUME IS {round(d,2)}")
