import time

SIZE = 4096
buffer = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

########### Populating buffer ###########

def line_Column_50x():
    for _ in range(50):
        for i in range(SIZE):
            for j in range(SIZE):
                buffer[i][j] = (i + j) % 256

def column_line_50x():
    for _ in range(50):
        for j in range(SIZE):
            for i in range(SIZE):
                buffer[i][j] = (i + j) % 256

########### Benchmarks ###########

def main():

    print("Starting row first")
    start_time = time.time()
    line_Column_50x()
    end_time = time.time()
    print(f"Ending row first: {end_time - start_time:.2f} seconds")

    print("\nStarting column first")
    start_time = time.time()
    column_line_50x()
    end_time = time.time()
    print(f"Ending Column first: {end_time - start_time:.2f} seconds")

