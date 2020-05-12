

from tda_lista import Lista, insertar, eliminar, busqueda, barrido, criterio


class Persona(object):

    def __init__(self, apellido, nombre, dni):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return self.apellido + " "+self.nombre + " "+ str(self.dni)


# persona = Persona('acosta', 'juan', 33)
# dic = persona.__dict__
# print('nombre' in dic)


lista = Lista()

persona = Persona('acosta', 'juan', 33)
insertar(lista, persona, 'apellido')
persona = Persona('perez', 'martin', 35)
insertar(lista, persona, 'apellido')
persona = Persona('perez', 'jorge', 36)
insertar(lista, persona, 'apellido')
persona = Persona('bonato', 'ana', 34)
insertar(lista, persona, 'apellido')

barrido(lista)

#perez martin
persona1 = eliminar(lista, 80, 'dni')

print('dato eliminado', persona1)
barrido(lista)

pos = busqueda(lista, 'perez', 'nombre')
print(pos.info)