
class nodoLista(object):

    def __init__(self):
        self.info = None
        self.sig = None

class Lista(object):

    def __init__(self):
        self.inicio = None
        self.tamanio = 0



def insertar(lista, dato):
    nodo = nodoLista()
    nodo.info = dato
    if(lista.inicio is None or lista.inicio.info>nodo.info):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        act = lista.inicio.sig
        ant = lista.inicio
        while(act is not None and act.info<nodo.info):
            act = act.sig
            ant = ant.sig

        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1    


def eliminar(lista, clave):
    pass



def busqueda(lista, clave):
    pass


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig
    

def tamanio(lista):
    return lista.tamanio


def lista_vacia():
    return lista.inicio is None


lista = Lista()

insertar(lista, 1)
insertar(lista, 3)
insertar(lista, 0)
insertar(lista, 5)
insertar(lista, 7)
insertar(lista, 2)
barrido(lista)
a = input()
insertar(lista, 4)
insertar(lista, 100)
barrido(lista)

pos = busqueda(lista, 6)
if(pos is not None):
    pass