
from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final

'''
cola1 = Cola()
cola2 = Cola()
print('cargar cola 1')
while tamanio(cola1)<5:
    dato = int(input("ingrese un número"))
    arribo(cola1, dato)
print('cargar cola 2')
while tamanio(cola2)<7:
    dato = int(input("ingrese un número"))
    arribo(cola2, dato)

#c1 0 1 3 4 5 34 60 67
#c2 99
# itereaciones 4-4
cant = tamanio(cola1)

for i in range (0, cant):
    if(en_frente(cola1)< en_frente(cola2)):
        mover_final(cola1)
    else:
        #dato1 = atencion(cola1)
        while(en_frente(cola1)>en_frente(cola2)):
            dato = atencion(cola2)
            arribo(cola1, dato)
        mover_final(cola1)

while(not cola_vacia(cola2)):
    dato = atencion(cola2)
    arribo(cola1, dato)

for i in range(0, tamanio(cola1)):
    print(mover_final(cola1))
'''
from random import randint
from time import sleep
'''
cola = Cola()

arribo(cola, [1, 10])
arribo(cola, [2, 3])
arribo(cola, [4, 5])

while not cola_vacia(cola):
    dato = atencion(cola)
    print('atendiendo proceso', dato[0])
    if(dato[1]>4.5):
        dato[1] = dato[1] - 4.5
        sleep(4.5)
        arribo(cola, dato)
    else:
        sleep(dato[1])
    # preguntar si quiere agregar proceso
    resp = input('quiere cargar proces S/N?')
    if(resp.upper() == 'S'):
        tiempo = float(input('ingrese tiempo del proceso'))
        arribo(cola,[randint(1, 500), tiempo])
'''

from random import choice
vehiculos = ['auto', 'camioneta', 'camion', 'colectivo']
costo = [47, 59, 71, 64]

puesto1 = Cola()
puesto2 = Cola()
puesto3 = Cola()
total1 = 0
total2 = 0
total3 = 0
for i in range (30):
    arribo(puesto1, (choice(vehiculos)))
    arribo(puesto2, (choice(vehiculos)))
    arribo(puesto3, (choice(vehiculos)))

while(not cola_vacia(puesto1)):
    vehiculo = atencion(puesto1)
    pos = vehiculos.index(vehiculo)
    total1 += costo[pos]
    
    vehiculo = atencion(puesto2)
    pos = vehiculos.index(vehiculo)
    total2 += costo[pos]

    vehiculo = atencion(puesto3)
    pos = vehiculos.index(vehiculo)
    total3 += costo[pos]

'''
from math import asin, sqrt, sin, cos, 
r = 6371000

formula = 2*r*asin(sqrt(sin((q1-q2)/2)**2 + cos(q1)*cos(q2) * sin((d1-d2)/2)**2 ))
'''

# from datetime import datetime
# from copy import copy

# tipos_aviones = ['carga', 'negocios', 'pasajeros']
# tiempo_despegue = [9, 3, 5]
# tiempo_aterrizaje = [12, 5, 10]


# cola_despegue = Cola()
# cola_aterrizaje = Cola()



# arribo(cola_despegue, ['airline', 'argentina', 'chile', 'carga', '07:00', '23:00'])
# arribo(cola_despegue, ['airline', 'argentina', 'india', 'pasajeros', '07:10', '23:00'])
# arribo(cola_despegue, ['airline', 'argentina', 'rusia', 'negocios', '07:17', '23:00'])

# arribo(cola_aterrizaje, ['airline', 'argentina', 'rusia', 'negocios', '07:00', '23:00'])

# hora_actual = datetime.now()

# while(not cola_vacia(cola_despegue) or not cola_vacia(cola_aterrizaje)):

#     hora_despegue = copy(hora_actual)
#     hora_despegue.hour = int(en_frente(cola_despegue)[4][0:2])
#     hora_despegue.min =int(en_frente(cola_despegue)[4][3:])

#     if(not cola_vacia(cola_aterrizaje) and hora_despegue<= hora_actual):
#         avion = atencion(cola_aterrizaje)
#         pos = tipos_aviones.index(avion[3])
#         tiempo = tiempo_aterrizaje[pos]
#         print('avion aterrizando...')
#         sleep(tiempo)
#     else:
#         avion = atencion(cola_despegue)
#         pos = tipos_aviones.index(avion[3])
#         tiempo = tiempo_despegue[pos]
#         print('avion despegando...')
#         sleep(tiempo)

#     hora_actual = datetime().now()
    # preguntar si quiere agregar

# cola = Cola()
# cola1 = Cola()

# arribo(cola, 'luke')
# arribo(cola, 'darth vader')
# arribo(cola, 'yoda')
# arribo(cola, 'chewbacca')
# arribo(cola, 'kylo ren')
# arribo(cola, 'jar jar binks')

# for i in range(tamanio(cola)):
#     print(mover_final(cola))

# while(not cola_vacia(cola)):
#     personaje = atencion(cola)
#     if(personaje == 'yoda'):
#         arribo(cola1, 'obi-wan kenobi')
#     elif(personaje == 'jar jar binks' and not cola_vacia(cola)):
#         atencion(cola)
#     arribo(cola1, personaje)

# cantidad = tamanio(cola)
# i = 0
# while(i<cantidad):
#     personaje = atencion(cola)
#     if(personaje == 'yoda'):
#         arribo(cola, 'obi-wan kenobi')
#     elif(personaje == 'jar jar binks' and i<cantidad-1):
#         atencion(cola)
#         i += 1
#     arribo(cola, personaje)
#     i += 1

# for i in range(tamanio(cola1)):
#     print(mover_final(cola1))

