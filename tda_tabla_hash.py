
from tda_lista import Lista, insertar, eliminar, busqueda, tamanio, barrido

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla


def agregar_tc(tabla, dato):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = dato
    else:
        #!completar
        print('colision aplicar sondeo')


def agregar_ta(tabla, dato):
    posicion = hash_diccionario(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato, 'palabra')


def quitar_ta(tabla, dato):
    posicion = hash_diccionario(dato, tabla)
    if(tabla[posicion] is not None):
        return eliminar(tabla[posicion], dato.palabra, 'palabra')
    else:
        return None


def quitar_tc(tabla, dato):
    dato = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion] == dato):
            dato = tabla[posicion]
            tabla[posicion] = None
            #! revisar si hay colision y realizar desplazamineto
        else:
            #! completar
            print('aplicar funcion colision seguir busco')
    return None


def buscar_ta(tabla, dato):
    posicion = hash_diccionario(dato, tabla)
    if(tabla[posicion] is not None):
        return busqueda(tabla[posicion], dato.palabra, 'palabra')
    else:
        return None


def buscar_tc(tabla, dato):
    pos = None
    posicion = hash(dato, tabla)
    if(tabla[posicion] is not None):
        if(tabla[posicion] == dato):
            pos = posicion
        else:
            #! completar
            print('aplicar funcion colision seguir busco')
    return pos


def hash(clave, tabla):
    return clave % len(tabla)


def bernstein(cadena):
    """Función hash de Bernstein para cadenas."""
    h = 0
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    return h


def cantidad_elementos_ta(tabla):
    cantidad = 0
    for elemento in tabla:
        if(elemento is not None):
            cantidad += tamanio(elemento)
    return cantidad
    #return sum(tamanio(lista) for lista in tabla if lista is not None)


def cantidad_elementos_tc(tabla):
    # cantidad = 0
    # for elemento in tabla:
    #     if(elemento is not None):
    #         cantidad += 1
    # return cantidad
    return len(tabla) - tabla.count(None)


def hash_diccionario(dato, tabla):
    return ord(dato.palabra[0].upper()) % len(tabla)
    
class Palabra(object):

    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
    
    def __str__(self):
        return self.palabra

tabla = crear_tabla(26)

# punto A
palabra = Palabra('hola', 'es un saludo')
agregar_ta(tabla, palabra)
palabra = Palabra('hielo', 'agua congelada')
agregar_ta(tabla, palabra)
palabra = Palabra('arbol', 'asdasdsadsda')
agregar_ta(tabla, palabra)
for i in tabla:
    if(i is not None):
        barrido(i)
print()
# punto B
pos = buscar_ta(tabla, Palabra('hola',''))
if(pos is not None):
    print('palabra', pos.info.palabra, 'significado', pos.info.significado)
print()
#punto C
print('elemento eliminado', quitar_ta(tabla, Palabra('hielo','')))

for i in tabla:
    if(i is not None):
        barrido(i)