# Write a Python program to remove an empty tuple(s) from a list of tuples. 
list1=[(), (), (), ('c', 'e'), ('ca', 'ea'), ('d',), ('do',), ('dog', 'ear', 'eat', 'cat', 
'car'), ('dogs', 'cars', 'done', 'eats', 'cats', 'ears'), ('don',)]
for i in list1:
    if len(i)==0:        # put the condition length of tuple equql to zero 
        list1.remove(i)
print(list1)        
