import random 
import os
import time

print("TESTE DE FOR")

for i in range(10):
    print(i)

time.sleep(10)

print("TESTE RANGE")

for i in range(1, 10, 1):
    print(i)

time.sleep(10)

print("TESTE RANDOM")

numero = random.randint(1, 10)
print(numero)

time.sleep(10)
os.system("clear")