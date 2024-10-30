import time

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

n1 = 5

# start = time.time()
# print(factorial(n1))
# end = time.time()

# print(f"Time: {end - start}")

def odd_nums(n):
    if n == 0:
        return 1
    else:
        return n*2 + 1 + odd_nums(n - 1)
    

n2 = 3

print(odd_nums(n2))