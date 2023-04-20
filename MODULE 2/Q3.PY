n=int(input("given element for fibonacci series:"))
a=0
b=1
c=a+b
print(f"{a}\n{b}")
i=3
while i<=n:      
    print(c)
    a=b
    b=c
    c=a+b
    i+=1
    

