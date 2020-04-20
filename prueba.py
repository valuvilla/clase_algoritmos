from tda_pila_dinamico import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint


pila = Pila()
pilapar = Pila()
pilaimpar = Pila()


archivo = open('datos.txt')

linea = archivo.readline()

print('archivo')
while linea:
    linea = linea.replace('\n', '')
    print(linea)
    apilar(pila, linea)
    linea = archivo.readline()

print('\npila')
while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)

'''
while tamanio(pila) <= 20:
    x = randint(1,100)
    print(x)
    apilar(pila, x)

while not pila_vacia(pila):
    x = desapilar(pila)
    if(x % 2 == 0):
        apilar(pilapar, x)
    else:
        apilar(pilaimpar, x)


print("pila par")
while not pila_vacia(pilapar):
    x = desapilar(pilapar)
    print(x)
print("pila impar")
while not pila_vacia(pilaimpar):
    x = desapilar(pilaimpar)
    print(x)

'''
