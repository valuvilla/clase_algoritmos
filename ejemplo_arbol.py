from tda_arbol_binario_avl import *


raiz = None
i=0
pais = input("Ingrese nombre del pais a cargar: ")
while(pais != "" and i < 5):
    raiz = insertar_nodo(raiz, pais)
    i+=1
    pais = input("Ingrese nombre del pais a cargar: ")

print("INORDEN".center(50, "-"))
inorden(raiz)
pais = input ("ingrese el pais a eliminar: ")
raiz, dato = eliminar_nodo(raiz, pais)
if dato is not None:
    print("El dato eliminado es: ", dato)

pos = busqueda(raiz, "Tailandia")
if pos is not None:
    raiz, dato = eliminar_nodo(raiz, "Tailandia")
    dato="Tailandia"
    raiz = insertar_nodo(raiz, dato)

print("INORDEN".center(50, "-"))
inorden(raiz)