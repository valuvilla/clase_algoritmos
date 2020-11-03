
from tda_cola import Cola, cola_vacia, arribo, atencion
from tda_pila import Pila, pila_vacia, apilar, desapilar, barrido
from tda_heap2 import Heap, arribo as arribo_h, atencion as atencion_h, heap_vacio, cambiar_prioridad
# , buscar as buscar_h
from math import inf


class nodoArista(object):
    """Clase nodo vértice."""

    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de arsitas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


def insertar_vertice(grafo, dato):
    """Inserta un vértice al grafo."""
    nodo = nodoVertice(dato)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1


def insertar_arista(grafo, dato, origen, destino):
    """Inserta una arista desde el vértice origen al destino."""
    agregrar_arista(origen.adyacentes, dato, destino.info)
    if(not grafo.dirigido):
        agregrar_arista(destino.adyacentes, dato, origen.info)


def agregrar_arista(origen, dato, destino):
    """Agrega la arista desde el vértice origen al destino."""
    nodo = nodoArista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while(act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1


def eliminar_vertice(grafo, clave):
    """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
    x = None
    if(grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while(act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if(x is not None):
        aux = grafo.inicio
        while(aux is not None):
            if(aux.adyacentes.inicio is not None):
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x


def eliminar_arista(vertice, destino):
    """Elimina una arsita del vertice y lo devuelve si lo encuentra."""
    x = None
    if(vertice.inicio.destino == destino):
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while(act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x


def buscar_vertice(grafo, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = grafo.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def buscar_arista(vertice, buscado):
    """Devuelve la direccion del elemento buscado."""
    aux = vertice.adyacentes.inicio
    while(aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux


def tamanio(grafo):
    """Devuelve el numero de vertices en el grafo."""
    return grafo.tamanio


def grafo_vacio(grafo):
    """Devuelve true si el grafo esta vacio."""
    return grafo.inicio is None


def marcar_no_visitado(grafo):
    """Marca todos losvertices del grafo como no visitados."""
    aux = grafo.inicio
    while(aux is not None):
        aux.visitado = False
        aux = aux.sig


def barrido_profundidad(grafo, vertice):
    """Barrido en profundidad del grafo."""
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while(adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if(not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_amplitud(grafo, vertice):
    """Barrido en amplitud del grafo."""
    cola = Cola()
    while(vertice is not None):
        if(not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            while(not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig


def barrido_vertices(grafo):
    """Realiza un barrido de la grafo mostrando sus valores."""
    aux = grafo.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig


def existe_paso(grafo, origen, destino):
    """Barrido en profundidad del grafo."""
    resultado = False
    if(not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while(vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if(adyacente.info == destino.info):
                return True
            elif(not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado


def adyacentes(vertice):
    """Muestra los adyacents del vertice."""
    aux = vertice.adyacentes.inicio
    while(aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig


def es_adyacente(vertice, destino):
    """Determina si el destino es adyacente directo."""
    resultado = False
    aux = vertice.adyacentes.inicio
    while(aux is not None and not resultado):
        if(aux.destino == resultado):
            resultado = True
        aux = aux.sig
    return resultado


def dijkstra(grafo, origen, destino):
    """Algoritmo de Dijkstra para hallar el camino mas corto."""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while(aux is not None):
        if(aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig

    while(not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while(aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux = aux.sig
    return camino


def kruskal(grafo):
    """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    aux = grafo.inicio
    while(aux is not None):
        bosque.append([aux.info])
        adyac = aux.adyacentes.inicio
        while(adyac is not None):
            arribo_h(aristas, [aux.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        aux = aux.sig
    while(len(bosque) > 1 and not heap_vacio(aristas)):
        dato = atencion_h(aristas)
        origen = None
        for elemento in bosque:
            if(dato[0] in elemento):
                origen = bosque.pop(bosque.index(elemento))
                break
        destino = None
        for elemento in bosque:
            if(dato[1] in elemento):
                destino = bosque.pop(bosque.index(elemento))
                break
        if(origen is not None and destino is not None):
            if(len(origen) > 1 and len(destino) == 1):
                destino = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) == 1):
                origen = [dato[0], dato[1]]
            elif(len(destino) > 1 and len(origen) > 1):
                origen += [dato[0], dato[1]]
            bosque.append(origen + destino)
        else:
            bosque.append(origen)
    return bosque[0]


def prim(grafo):
    """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
    bosque = []
    aristas = Heap(tamanio(grafo) ** 2)
    adyac = grafo.inicio.adyacentes.inicio
    while(adyac is not None):
        arribo_h(aristas, [grafo.inicio.info, adyac.destino], adyac.info)
        adyac = adyac.sig
    while(len(bosque) // 2 < tamanio(grafo) and not heap_vacio(aristas)):
        dato = atencion_h(aristas)

        if(len(bosque) == 0 or ((dato[0] not in bosque) ^ (dato[1] not in bosque))):
            bosque += dato
            destino = buscar_vertice(grafo, dato[1])
            adyac = destino.adyacentes.inicio
            while(adyac is not None):
                arribo_h(aristas, [destino.info, adyac.destino], adyac.info)
                adyac = adyac.sig
    return bosque


g = Grafo(False)
insertar_vertice(g, "A")
insertar_vertice(g, "B")
insertar_vertice(g, "F")
insertar_vertice(g, "C")
insertar_vertice(g, "Z")
insertar_vertice(g, "E")
insertar_vertice(g, "P")
insertar_vertice(g, "K")
insertar_vertice(g, "V")
insertar_vertice(g, "S")
insertar_vertice(g, "T")

origen = buscar_vertice(g, "T")
destino = buscar_vertice(g, "A")
if(origen is not None and destino is not None):
    insertar_arista(g, 5, origen, destino)

origen = buscar_vertice(g, "E")
destino = buscar_vertice(g, "Z")
if(origen is not None and destino is not None):
    insertar_arista(g, 10, origen, destino)

origen = buscar_vertice(g, "E")
destino = buscar_vertice(g, "A")
if(origen is not None and destino is not None):
    insertar_arista(g, 12, origen, destino)

pos = buscar_vertice(g, "E")
pos_aux = buscar_arista(pos, "B")
if(pos_aux is not None):
    print("esta", pos_aux.info, pos_aux.destino)
else:
    print("no esta")

origen = buscar_vertice(g, 'C')
destino = buscar_vertice(g, 'Z')
if(origen is not None and destino is not None):
    insertar_arista(g, 9, origen, destino)

origen = buscar_vertice(g, 'Z')
destino = buscar_vertice(g, 'P')
if(origen is not None and destino is not None):
    insertar_arista(g, 15, origen, destino)

origen = buscar_vertice(g, 'A')
destino = buscar_vertice(g, 'B')
if(origen is not None and destino is not None):
    insertar_arista(g, 150, origen, destino)

origen = buscar_vertice(g, 'A')
destino = buscar_vertice(g, 'F')
if(origen is not None and destino is not None):
    insertar_arista(g, 80, origen, destino)

origen = buscar_vertice(g, 'F')
destino = buscar_vertice(g, 'Z')
if(origen is not None and destino is not None):
    insertar_arista(g, 160, origen, destino)

origen = buscar_vertice(g, 'B')
destino = buscar_vertice(g, 'C')
if(origen is not None and destino is not None):
    insertar_arista(g, 100, origen, destino)

origen = buscar_vertice(g, 'Z')
destino = buscar_vertice(g, 'A')
if(origen is not None and destino is not None):
    insertar_arista(g, 175, origen, destino)

origen = buscar_vertice(g, 'K')
destino = buscar_vertice(g, 'V')
if(origen is not None and destino is not None):
    insertar_arista(g, 75, origen, destino)

origen = buscar_vertice(g, 'Z')
destino = buscar_vertice(g, 'K')
if(origen is not None and destino is not None):
    insertar_arista(g, 20, origen, destino)

origen = buscar_vertice(g, 'E')
destino = buscar_vertice(g, 'F')
if(origen is not None and destino is not None):
    insertar_arista(g, 13, origen, destino)

origen = buscar_vertice(g, 'F')
destino = buscar_vertice(g, 'K')
if(origen is not None and destino is not None):
    insertar_arista(g, 3, origen, destino)

origen = buscar_vertice(g, 'S')
destino = buscar_vertice(g, 'K')
if(origen is not None and destino is not None):
    insertar_arista(g, 25, origen, destino)

origen = buscar_vertice(g, 'V')
destino = buscar_vertice(g, 'S')
if(origen is not None and destino is not None):
    insertar_arista(g, 49, origen, destino)

camino = dijkstra(g, 'A', 'S')

fin = 'B'
while(not pila_vacia(camino)):
    dato = desapilar(camino)
    if(fin == dato[1][0].info):
        print("de", dato[1][0].info, "hasta", dato[1][1], dato[0])
        fin = dato[1][1]

# print("de", dato[1][0].info, "hasta", dato[1][1], dato[0])
# barrido(camino)
# print(kruskal(g))
# print(prim(g))

# def cargar_grafo(grafo):
#     pass


# grafo = Grafo(False)
# cargar_grafo(grafo)

# barrido_profundidad(grafo, grafo.inicio)
# marcar_no_visitado(grafo)
# barrido_amplitud(grafo, grafo.inicio)

# origen = buscar_vertice(grafo, 'T')
# destino = buscar_vertice(grafo, 'Z')
# camino_mas_corto = None
# if(origen is not None and destino is not None):
#     if(existe_paso(grafo, origen, destino)):
#         camino_mas_corto = dijkstra(grafo, 'T', 'Z')
#         fin = destino.info
#         while(not pila_vacia(camino_mas_corto)):
#             dato = desapilar(camino_mas_corto)
#             if(fin == dato[1][0].info):
#                 print(dato[1][0].info)
#                 fin = dato[1][1]

# marcar_no_visitado(grafo)
# arbol_minimo = kruskal(g)
# print(arbol_minimo)
# arbol_minimo = prim(g)
# print(arbol_minimo)

"""
print("amplitud")
barrido_amplitud(g, g.inicio)
marcar_no_visitado(g)
print("profundidad")
barrido_profundidad(g, g.inicio)
origen = buscar_vertice(g, 'E')
eliminar_vertice(g, "Z")
barrido_vertices(g)
adyacentes(origen)
"""