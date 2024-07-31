def fibonacci(n):
    sequence = [0, 1]
    while sequence[len(sequence)-1] < n:
        sequence.append(sequence[len(sequence)-1] + sequence[len(sequence)-2])
    return sequence

num = int(input("Enter a number: "))
fib_sequence = fibonacci(num)
print(fib_sequence[len(fib_sequence)-2]) 