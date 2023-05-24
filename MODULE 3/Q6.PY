# How will you compare two lists? 
list1=[]
list2=[]
n=int(input("enter no of element in list 1 & 2 :"))
for i in range(n):
    element1=int(input("enter element of list1 :"))      # FOR INPUT LIST1
    list1.append(element1)
print(list1)
for i in range(n):
    element2=int(input("enter element of list2 :"))      # FOR INPUT LIST2
    list2.append(element2)
print(list2)
if list1.sort()==list2.sort():     #FOR COMPARE SORTING IN ASCENDING ORDER BOTH LIST
    print("BOTH ARE EQUAL")
else:
    pritn("BOTH ARE NOT EQUAL")    

    
    
   
