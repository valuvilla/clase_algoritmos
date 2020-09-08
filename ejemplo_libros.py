from tda_archivo import abrir, cerrar, guardar, leer


class Libro():

    def __init__(self, isbn, titulo, autores, editorial, cant):
        self.isbn = isbn
        self.titulo = titulo
        self.autores = autores
        self.editorial = editorial
        self.cant = cant

file = abrir('libros')

# l1 = Libro('123', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('234', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('567', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('890', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('012', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
# l1 = Libro('033', 'algoritmos', 'nuevo', 'uader', 230)
# guardar(file, l1)
pos = 0

while(pos<len(file)):
    libro = leer(file, pos)
    print(libro)
    print(libro.isbn, libro.cant, libro.titulo)
    pos += 1

cerrar(file)

