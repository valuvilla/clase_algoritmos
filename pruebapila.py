from tda_pila_dinamico import Pila, pila_vacia, desapilar, apilar, tamanio, cima
from random import randint


class Carta():

    def __init__(self):
        self.numero = None
        self.palo = None

pila = Pila()

carta = Carta()
carta.numero = int(input('ingrese el numero de la carta') )
carta.palo = input('ingrese el palo de la carta')

apilar(pila, carta)

dato = desapilar(pila)
print(dato.numero, dato.palo)






'''
pila_personajes = Pila()

archivo = open('personajes')

linea = archivo.readline()

print('archivo')
while linea:
    linea = linea.replace('\n', '')
    linea = linea.split(';')
    linea[0] = linea[0].title()
    linea[1] = int(linea[1])
    #print(linea)
    apilar(pila_personajes, linea)
    linea = archivo.readline()

i = 1
while(not pila_vacia(pila_personajes)):
    personaje = desapilar(pila_personajes)
    if(personaje[0] == 'Rocket Raccoon' or personaje[0] == 'Groot'):
        print(personaje[0], 'esta en la posicion', i)
    if(personaje[1]>5):
        print(personaje[0], 'participo en mas de 5 peliculas')
    if(personaje[0] == 'Black Widow'):
        print(personaje[0], 'participo en', personaje[1], 'peliculas')
    if(personaje[0][0] in ['C', 'D', 'G']):
        print('comienza con', personaje[0])
    i += 1 
'''

'''
pila = Pila()
pila_aux = Pila()

while(not pila_llena(pila)):
    apilar(pila, randint(0, 100))

print("pila normal")
while(not pila_vacia(pila)):
    x = desapilar(pila)
    apilar(pila_aux, x)
    print(x)


pila = pila_aux

print("pila invertida")
while(not pila_vacia(pila)):
    print(desapilar(pila))
'''











'''
ep5 = Pila()
ep7 = Pila()
paux = Pila()

while not pila_llena(ep5):
    x = input('ingrese nombre personaje ')
    apilar(ep5, x)


while not pila_llena(ep7):
    x = input('ingrese nombre personaje ')
    apilar(ep7, x)

print("interseccion")
while(not pila_vacia(ep5)):
    x = desapilar(ep5)
    while(not pila_vacia(ep7)):
        xaux = desapilar(ep7)
        if(x == xaux):
            print(x)
        apilar(paux, xaux)
    while(not pila_vacia(paux)):
        xaux = desapilar(paux)
        apilar(ep7, xaux)
'''

"""
num = int(input('engrese el numero del elemento a modificar '))


if(tamanio(pila)>num+1):
    i = 0
    while i<num:
        x = desapilar(pila)
        apilar(pilaaux, x)
        i += 1
    x = desapilar(pila)
    print('elemento eliminado', x)
    while not pila_vacia(pilaaux):
        x = desapilar(pilaaux)
        apilar(pila,x)


print("pila")
while not pila_vacia(pila):
    x = desapilar(pila)
    print(x)
"""



