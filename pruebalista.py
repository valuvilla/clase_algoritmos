from tda_lista import Lista, insertar, eliminar, busqueda, barrido, lista_vacia
from random import randint

lista_uno = Lista()
lista_dos = Lista()

for i in range(10):
    insertar(lista_uno, randint(0, 50))

for i in range(43):
    insertar(lista_dos, randint(0, 50))

aux = lista_uno.inicio
barrido(lista_uno)

while(aux is not None):
    pos = busqueda(lista_dos, aux.info)
    if(pos is not None):
        print(aux.info)
    aux = aux.sig



# for i in range(30):
#     insertar(lista_uno, randint(0, 50))

# barrido(lista)

# while(not lista_vacia(lista)):
#     dato = eliminar(lista, lista.inicio.info)
#     if(dato % 2 == 0):
#         insertar(lista_par, dato)
#     else:
#         insertar(lista_impar, dato)

# aux = lista.inicio

# while(aux is not None):
#     if(aux.info % 2 == 0):
#         insertar(lista_par, aux.info)
#     else:
#         insertar(lista_impar, aux.info)
#     aux= aux.sig

# print('par')
# barrido(lista_par)
# print('impar')
# barrido(lista_impar)
lista = Lista()
for i in range(100):
    insertar(lista, chr(randint(65, 90)))


barrido(lista)

dato = eliminar(lista, 'A')
while(dato is not None):
    dato = eliminar(lista, 'A')

dato = eliminar(lista, 'E')
while(dato is not None):
    dato = eliminar(lista, 'E')

dato = eliminar(lista, 'I')
while(dato is not None):
    dato = eliminar(lista, 'I')

dato = eliminar(lista, 'O')
while(dato is not None):
    dato = eliminar(lista, 'O')

dato = eliminar(lista, 'U')
while(dato is not None):
    dato = eliminar(lista, 'U')
print()
barrido(lista)

