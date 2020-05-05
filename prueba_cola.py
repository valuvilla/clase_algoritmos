
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

from time import sleep
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
    if(vehiculo=='auto'):
        total2 += 47
    elif(vehiculo=="camioneta"):
        total2 += 57
    vehiculo = atencion(puesto3)
    if(vehiculo=='auto'):
        total3 += 47
    elif(vehiculo=="camioneta"):
        total3 += 57


from math import asin, sqrt, sin, cos, 
r = 6371000

formula = 2*r*asin(sqrt(sin((q1-q2)/2)**2 + cos(q1)*cos(q2) * sin((d1-d2)/2)**2 ))
'''