print("printing the floyd's triangle")
n=int(input("enter the number of rows required"))
num=1
for i in range(n):
    for j in range(i+1):
        print(num, end=' ')
        num=num+1
    print()   

      