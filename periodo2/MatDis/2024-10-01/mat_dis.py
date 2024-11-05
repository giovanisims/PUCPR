def checkprime(n):
    if n < 2:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True

s = {2,3,4,5,6}

a = set()
b = set()
c = set()

for i in s:
    if i % 2 != 0:
        a.add(i)
    if 2 <= i < 4:
        b.add(i)
    if checkprime(i):
        c.add(i)

print(a)
print(b)
print(c)