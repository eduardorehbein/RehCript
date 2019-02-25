from conversor32 import Conversor32
from random import randint

numeros1 = list()

for i in range(50):
    numeros1.append(randint(0, 10000000000))

c = Conversor32()
numeros2 = list(map(lambda x: c.decParaBase32(x), numeros1))
#numeros3 = list(map(lambda x: c.decParaBase32v2(x), numeros1))

print(numeros2)
#print(numeros3)
#if numeros2 == numeros3:
#    print("Deu certo")
#else:
#    print("Não funfou")
