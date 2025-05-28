import threading
import time
import random

print("Threads running")

def mythread(n):
    t = random.randint(1,3)
    time.sleep(t)
    print(f"Thread {n} active after {t} seconds")

for i in range(10):
    threading.Thread(target=mythread, args=(i,)).start()

