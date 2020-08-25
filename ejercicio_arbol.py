
from tda_archivo import abrir, leer, cerrar, guardar
from tda_arbol_bin import insertar_nodo, inorden, por_nivel, busqueda

arbol_nombre = None
arbol_ranking = None
arbol_especie = None

file = abrir('jedis')
pos = 0
while (pos <len(file)):
    jedi = leer(file, pos)
    arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
    arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
    arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
    pos += 1

cerrar(file)

#b
# inorden(arbol_nombre)
# a=input()

#c
# por_nivel(arbol_especie)
# a=input()

#d
pos = busqueda(arbol_nombre, 'luke skywalker')

if(pos is not None):
    file = abrir('jedis')
    jedi = leer(file, pos.nrr)
    cerrar(file)
    print(jedi)