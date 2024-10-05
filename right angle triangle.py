print("Half pyramid pattern of stars")
n=int(input("enter the number of rows required:--"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()    
    
