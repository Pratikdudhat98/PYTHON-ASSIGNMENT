# Write a Python function to get the largest number, smallest num and sum of all from a list.
list1=[]
n=int(input("NO OF ELEMENT IN LIST :"))
for i in range(n):
    element=int(input())  # INPUT ELEMENT
    list1.append(element)
print(list1)
print(f"MAXIMUM NO IS {max(list1)}")   # FOR MAX NO
print(f"MINIMUM NO IS {min(list1)}")    # FOR MIN NO 
print(f"SUM OF LIST IS {SUM(list1)}")    # FOR SUM OF NO
