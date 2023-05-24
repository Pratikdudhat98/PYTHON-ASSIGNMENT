# Write a Python script to sort (ascending and descending) a dictionary by value. 
dic1={1:456,7:567,4:789,3:984,6:154,9:698}
dic2={}
dic3={}
dic1=dic1.items()
asc=list(dic1)
dsc=list(dic1)
asc.sort()
dsc.sort(reverse=True)
dic2=dict(asc)
dic3=dict(dsc)
print(f"ascending {dic2}")
print(f"descending {dic3}")


    