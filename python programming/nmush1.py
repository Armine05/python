a=[]
for  i in range(3):
    b=int(input("insert number"))
    a.append(b)
    
max=a[0]
if(max<a[1]):
    max=a[1]
if(max<a[2]):
    max=a[2]
print(max)
    
