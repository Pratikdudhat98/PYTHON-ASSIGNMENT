# Write a Python function that takes two lists and returns true if they have at least one common member.
list1=[]
list2=[]
n=int(input("no of element in list:"))
for i in range(n):
    element1=int(input("enter element1:"))   # FOR ENTER LIST 1 ELEMENT
    element2=int(input("enter element2:"))    # FOR ENTER LIST 2 ELEMENT 
    list1.append(element1)
    list2.append(element2)
print(list1)
print(list2)
for x in list1:
    for y in list2:
        if x==y :           # AT LEAST ONE COMMEN ELEMENT 
           re=True
        else :
           re=False   
print(re)                   