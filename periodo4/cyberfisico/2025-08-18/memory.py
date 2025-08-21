def f(n, L):
    print (n, len(L))
    if n > 0:
        L2 = []
        for i in range(2*len(L)):
            L2.append(i)
        f(n-1, L2)

a = [1,2,3,4,5,6,7,8,9,10]

b = a
del (a)

def g(x):
    a = x

g(11)

# print(a)
print(b)

i = 0
while i <= 10:
    print(b[1])
    i += 1

f(100, b)