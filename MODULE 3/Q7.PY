# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
list1=[]
number=0
n =int(input("no of element in list :"))      # FOR NO OF ELEMENT INPUT
for i in range(n):
    element=input("enter string:")             # FOR ELEMENT INPUT
    list1.append(element)
    if len(element)>=2 and element[0]==element[-1]: # FOR string length is 2 or more and the first and last character are same
        number+=1
print(list1)
print(number)
        
