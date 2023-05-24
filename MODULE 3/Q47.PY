"""Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
Counter ({'item1': 1150, 'item2': 300})"""  
list1=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] 
list2={}
for i in list1:
    if i['item'] in list2:
        list2[i['item']]+=i['amount'] 
    else:
        list2[i['item']]=i['amount']
print(list2)

    
