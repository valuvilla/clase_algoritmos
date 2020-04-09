from tda_pila import Pila, pila_llena, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint


pila = Pila()
pilapar = Pila()
pilaimpar = Pila()

while not pila_llena(pila):
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


