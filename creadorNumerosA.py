import os
import random

archivo=open('na.txt','w')
lista_aleatorios=[]

for i in range(1,10000000):
    i=random.randint(1,1000)
    lista_aleatorios.append(i)
    archivo.write(str(i)+'\n')

archivo.close()