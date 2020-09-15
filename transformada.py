
from tda_arbol_bin import busqueda_nario, nodoArbolGreek, insertar_nario, preorden, por_nivel_nario, inorden

arbol = None


archivo = open('greek_gods')

linea = archivo.readline()

print('archivo')
while linea:        
    linea = linea.replace('\n', '')
    dios = linea.split(';')
    nodo = nodoArbolGreek(dios[0], dios[2])
    #print('insertar', dios[0])
    if(arbol is None):
        arbol = nodo
    else:
        pos = []
        busqueda_nario(arbol, dios[1], pos)
        #print('resultado de busqueda', pos[0].info)
        insertar_nario(pos[0], nodo)

    #preorden(arbol)
    #a = input()
    linea = archivo.readline()


archivo.close()

#por_nivel_nario(arbol)

# pos = []
# busqueda_nario(arbol, 'zeus', pos)

# hijo = pos[0].izq

# while(hijo is not None):
#     print(hijo.info)
#     hijo = hijo.der

bosque = []
hijo = arbol.izq

while(hijo is not None):
    aux = hijo.der
    hijo.der = None
    bosque.append(hijo)
    hijo = aux

print('cantidad de arboles del bosque', len(bosque))
for arbol in bosque:
    print('raiz ------------------>', arbol.info)
    inorden(arbol)
    print()



