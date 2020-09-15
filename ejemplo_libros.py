
#! ejercicio 21 lunes
#! hacer ejercicio 12 martes


from tda_archivo import abrir, cerrar, guardar, leer
from tda_arbol_binario_avl import insertar_nodo, inorden, preorden, busqueda, busqueda_proximidad_archivo
from tda_arbol_binario_avl import busqueda_archivo

class Libro():

    def __init__(self, isbn, titulo, autores, editorial, cant):
        self.isbn = isbn
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.cant = cant

file = abrir('libros')

# l1 = Libro('123', 'algoritmos', 'autor1;autor2', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('234', 'algoritmos', 'autor1;autor2;autor3;autor4', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('567', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('890', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('012', 'pyhton', 'nuevo', 'uader', 1000)
# guardar(file, l1)
# l1 = Libro('033', 'datos', 'nuevo', 'uader', 890)
# guardar(file, l1)

arbol_isbn = None
arbol_titulo = None
arbol_autores = None

pos = 0

while(pos<len(file)):
    libro = leer(file, pos)
    print(libro.isbn, libro.cant, libro.titulo)
    #print(libro.autores.split(';'))
    arbol_isbn = insertar_nodo(arbol_isbn, libro.isbn, pos)
    arbol_titulo = insertar_nodo(arbol_titulo, libro.titulo, pos)
    for autor in libro.autores.split(';'):
        arbol_autores = insertar_nodo(arbol_autores, autor, pos)
    pos += 1

cerrar(file)

pos = busqueda(arbol_isbn, '567')
if(pos is not None):
    file = abrir('libros')
    libro = leer(file, pos.nrr)
    cerrar(file)
    print(libro.isbn, libro.cant, libro.titulo, libro.autores)
print()
file = abrir('libros')
busqueda_proximidad_archivo(arbol_titulo, 'p', file)
cerrar(file)

print()
file = abrir('libros')
busqueda_archivo(arbol_titulo, 229, file)
cerrar(file)

print()
file = abrir('libros')
busqueda_proximidad_archivo(arbol_autores, 'autor1', file)
cerrar(file)
