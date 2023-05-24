# Write a Python program to find the highest 3 values in a dictionary 
dic1={1:897,6:877,14:457,25:879,12:564,89:7458}
dic1=dic1.values()
dic1=list(dic1)
dic1.sort()
print(f"1st highest :{dic1[-1]}\n2nd highest :{dic1[-2]}\n3rd highest :{dic1[-3]}")