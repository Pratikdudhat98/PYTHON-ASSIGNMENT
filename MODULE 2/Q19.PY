a=input("ENTER STRING :")
b=a.find("not")
c=a.find("poor")
if b < c :
    print(a.replace(a[b:c+4],"good"))
