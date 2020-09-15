
from tda_arbol_binario_avl import insertar_nodo, altura, cortar_por_nivel, inorden, contar
from random import randint

arbol = None

for i in range(1,1024):
    arbol = insertar_nodo(arbol, i)

cantidad = [0]
contar(arbol, cantidad)
print(altura(arbol), cantidad[0])

bosque = []
cortar_por_nivel(arbol, bosque)

print(len(bosque))

for arbol in bosque:
    print('raiz del arbol', arbol.info)
    cantidad = [0]
    contar(arbol, cantidad)
    print('cantidad de nodos del arbol', cantidad[0])
    