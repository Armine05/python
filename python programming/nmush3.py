def myfunc(x):
    if x < 2:
        return False

    i = 2
    while i <= x/2:
        if x % i == 0:
            return False
        i = i + 1

    return True


a = []

for i in range(100):
    a.append(i)

for i in a:
    if myfunc(i) == True:
        print(i)
