print("loops")
num=int(input("insert number"))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
    if i==5:
        break
else:
    print("all iterations of the loop are executed")
print("the sum is",sum)
