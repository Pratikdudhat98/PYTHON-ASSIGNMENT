# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
list1=[]
listunique=[]
n=int(input("enter no of element in list:"))   # FOR NO OF ELEMENT INPUT
for i in range(n):
    element=int(input("enter element:"))    # FOR ENTER ELEMENT
    list1.append(element)
    if element not in listunique:       # CONDITION FOR UNIQUE LIST
        listunique.append(element)
print(f"list is {list1}")
print(f"unique list is {listunique}")    # PRINT UNIQUE LIST

