from tda_pila import Pila, pila_llena, pila_vacia, desapilar, apilar, tamanio, cima


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



