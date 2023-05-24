# How Do You Check The Presence Of A Key In A Dictionary?
"""The keys () method takes no arguments and returns an object that represents a list of all the keys present in a particular
 input dictionary. So, in order to check whether a particular key is present in the dict, we use Python if statement along with 
 the keys () method to compare the search_key with the list of keys returned from the keys () method."""

dic1={1:897,6:897,14:457,25:879,12:564,89:7458}
n=int(input("enter key :"))       # FOR INPUT OF KEY
dic1=dic1.keys()            # CONVERT IN LIST OF KEYS
if n in dic1:
    print("this key presence in dictionary")    # PRINT IF PRESENCE
else:
    print("this key not presence in dictionary")    # PRINT IF NOT PRESENCE
