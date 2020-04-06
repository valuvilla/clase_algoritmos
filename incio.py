
from recursividad import sumaR, bbin, quicksort

print("hola walter")

# ejercicio 1
'''
num1 = ('ingrese un valor')
print(sumaR(num1))
'''
a1 = 2
r = -3


def progresion(cantidad):
    if(cantidad == 1):
        return 2
    else:
        return -3 * progresion(cantidad-1)


# ejercicio 2
bus = 101
vec = [3, 5, 11, 14, 17, 20, 45, 100, 23, 8]

#print(bbin(vec, bus, 0, len(vec)))


#print(bbin(vec, bus, 0, len(vec)-1))

izq = 5
der = 5
pivote = 9

vec = [1, 20, 10, 12, 9, 23, 210, 130, 40, 56]


# vec = [['123, 234', 'canion', 'fallo'], ['123, 234', 'canion', 'fallo'], ['123, 234', 'canion', 'derribado']]

palabra = "holaaaa"

def invertir(cadena):
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[len(cadena)-1] + invertir(cadena[0:len(cadena)-1])

print(invertir(palabra))

matriz = [[0, 0, 0, 0],
          [1, 0, 1, 0],
          [1, 0, 1, 0],
          [0, 0, 0, 0] ]

quicksort(vec, 0, len(vec)-1)
print(vec)



#MERGE SORT
vec = [5, 8, 11, 14, 17, 20, 23, 30, 45, 100]


def mergesort(lista):
    """Método de ordenamiento mergesort."""
    if (len(lista) <= 1):
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)
        if(izquierda[medio-1] <= derecha[0]):
            izquierda += derecha
            return izquierda
        resultado = merge(izquierda, derecha)
        return resultado

def merge(izquierda, derecha):
    """Función para mezclar listas."""
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha) > 0):
        if (izquierda[0] < derecha[0]):
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if(len(izquierda) > 0):
        lista_mezclada += izquierda
    if(len(derecha) > 0):
        lista_mezclada += derecha
    return lista_mezclada


# TDA TIPO DATO ABSTRACTO   DATO + FUNCIONALIDAD


from tda_polinomio import crear_polinomio, sumar_polinomios, modificar_termino

pol1 = [3, 5, 0, 6]
modificar_termino(pol1, 2, 4)
pol2 = [1, 2, 1,] 

print(sumar_polinomios(pol1, pol2))



from tda_archivo import abrir, cerrar, escribir, leer, modificar

arch = abrir('datos')
modificar(arch, 1, "hola")
#escribir(arch, 230)
#escribir(arch, 199)
for i in range(0, len(arch)):
    print(leer(arch, i))


cerrar(arch)
