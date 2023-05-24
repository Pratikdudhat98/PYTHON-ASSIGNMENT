# Write a python program to sum of the first n positive integers.
n=int(input("ENTER NUMBER :")) # FOR INPUT
sum=0
for i in range(1,n+1):
    sum=sum+i               # FOR EACH ITERATION SUM
    print(i,end=" ")        # FOR ITERATION PRINT   
print(f"sum is {sum}")      # FOR SUM PRINT
    