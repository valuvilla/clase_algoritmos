from tda_pila_dinamico import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint, choice


pila = Pila()
pilaaux = Pila()
pilapar = Pila()
pilaimpar = Pila()
mazo = Pila()


palos = ['espada', 'basto', 'copa', 'oro']


while(tamanio(mazo)<40):
    dato = ['', 0]
    dato[0] = choice(palos)
    dato[1] = randint(1, 12)
    apilar(mazo, dato)


while(not pila_vacia(mazo)):
    print(desapilar(mazo))

'''
dato = int(input('ingrese un numero '))
while dato != 0:
    if(pila_vacia(pila)):
        apilar(pila, dato)
    else:
        if(cima(pila) <= dato):
            apilar(pila, dato)
        else:
            while(not pila_vacia(pila) and cima(pila) > dato):
                daux = desapilar(pila)
                apilar(pilaaux, daux)
            apilar(pila, dato)
            while(not pila_vacia(pilaaux)):
                daux = desapilar(pilaaux)
                apilar(pila, daux)

    dato = int(input('ingrese un numero '))


while(not pila_vacia(pila)):
    print(desapilar(pila))
'''

'''
archivo = open('datos')

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
