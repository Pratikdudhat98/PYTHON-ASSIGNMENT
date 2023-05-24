# Write a Python function that takes a list of words and returns the length Of the longest one.
list1=["try","apple","job","poling","tops_technologies"]
list2=[]
for x in list1:
    list2.append((len(x),x))  # TUPLE APPEND IN LIST2
list2.sort()              # SORTING AFTER APPEND TUPLE
print(f"longest word is {list2[-1][0]} length is {list2[-1][1]}")  # PRINT
