import time
from threading import Thread

# # 1.Sem thread
# while True:
#     print('Estou rodando...')
#     time.sleep(.5)
# 2.Thread Simples

# def minhaThread():
#     for _ in range(0, 10):
#         time.sleep(2)
#         print('Oi... estou aqui também')
# Thread(target=minhaThread).start()
# while True:
#     print('Estou rodando...')
#     time.sleep(.5)

# # 3.Multiplas Threads
# def minhaThread(parametro, t):
#     for _ in range(0, 10):
#         time.sleep(t)
#         print(parametro)
# Thread(target=minhaThread, args=('T1: Oi... estou aqui também ', 1)).start()
# Thread(target=minhaThread, args=('T2: Sou a segunda Thread... ', .5)).start()
# while True:
#     print('Estou rodando...')
#     time.sleep(.5)