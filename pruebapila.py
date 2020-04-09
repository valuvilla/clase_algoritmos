from tda_pila import Pila, pila_llena, pila_vacia, desapilar, apilar, tamanio, cima


pila = Pila()
pilaaux = Pila()

while not pila_llena(pila):
    x = input('ingrese una palabra ')
    apilar(pila, x)


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




