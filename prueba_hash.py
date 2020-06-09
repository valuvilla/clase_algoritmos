

from tda_tabla_hash import crear_tabla, agregar_ta, bernstein_troopers, hash_division_troopers, bernstein, hash_division
from random import choice, randint
from tda_lista import barrido


letras = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legion = crear_tabla(10)
tabla_codigos = crear_tabla(1000)

class Stormtrooper(object):

    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo
    
    def __str__(self):
        return self.legion+' '+str(self.codigo)

for i in range(1,2000):
    legion = choice(letras)
    codigo = randint(1000, 9999)
    trooper = Stormtrooper(legion, codigo)
    agregar_ta(tabla_legion, bernstein_troopers, trooper, 'legion')
    agregar_ta(tabla_codigos, hash_division_troopers, trooper, 'codigo')


posicion = bernstein('FN', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = bernstein('CT', tabla_legion)
if(tabla_legion[posicion]):
    barrido(tabla_legion[posicion])
print()
posicion = hash_division(537, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])
print()
posicion = hash_division(781, tabla_codigos)
if(tabla_codigos[posicion]):
    barrido(tabla_codigos[posicion])