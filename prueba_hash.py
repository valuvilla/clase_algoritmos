

from tda_tabla_hash import crear_tabla, agregar_ta, bernstein_troopers, hash_division_troopers, bernstein_palabra, hash_division, hash_cifrado
from random import choice, randint
from tda_lista import barrido
from tda_tabla_hash import buscar_ta, Palabra



tabla = crear_tabla(10)

tabla2 = crear_tabla(10)

def desifrar(dato):
    dic = {"#?&": '0',"abc": '1',"def":'2',"ghi":'3',"jkl":'4',"mnñ":'5',"opq":'6',"rst":'7',"uvw":'8',"xyz":'9'}
    cadena = ''
    for i in range (0, len(dato),3):
        cadena += dic[dato[i:i+3]]
    return chr(int(cadena))



def cifrar(dato):
    valor = str(ord(dato))
    valor_cirado = ["#?&","abc","def","ghi","jkl","mnñ","opq","rst","uvw","xyz"]

    cadena = ""
    for num in valor:
        numInt = int(num)
        cadena += valor_cirado[numInt]
    cadena += "%"
    return cadena

a = 'Holaaaaaaaaa Mundo des tda hash'
a_cifrado = ''
for letra in a:
    valor = buscar_ta(tabla, hash_cifrado, Palabra(letra, ''), 'palabra')
    cifrado = ''
    if(valor is None):
        cifrado = cifrar(letra)
        palabra = Palabra(letra, cifrado)
        agregar_ta(tabla, hash_cifrado, palabra, 'palabra')
    else:
        cifrado = valor.info.significado
    a_cifrado += cifrado


print(a_cifrado)

lista = a_cifrado.split('%')
lista.pop()

msj = ''
for letras in lista:
    valor = buscar_ta(tabla2, bernstein_palabra, Palabra(letras, ''), 'palabra')
    decifrado = ''
    if(valor is None):
        decifrado = desifrar(letras)
        palabra = Palabra(letras, decifrado)
        agregar_ta(tabla2, bernstein_palabra, palabra, 'palabra')
    else:
        decifrado = valor.info.significado
    msj += decifrado

print(msj)

# for i in tabla:
#     print(i)

#print(a_cifrado)
#valor = buscar_ta(tabla, hash_cifrado, Palabra('H', ''), 'palabra')

#print(valor.info.significado)


'''
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
'''