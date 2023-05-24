# Write a Python program to check multiple keys exists in a dictionary .
dic1={1:897,6:897,14:457,25:879,12:564,89:7458}
dic2={4:254,5:779}
dic1.keys()                 # CONVERT IN KEY LIST
dic2.keys()            
if set(dic1).intersection(set(dic2)):    # CONVERT IN SET AND THROUGH INTERSECTION CHECK
    print("keys are exist")
else:
    print("keys are not exist")    