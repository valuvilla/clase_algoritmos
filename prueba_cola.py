
from tda_cola_dinamico import Cola, cola_vacia, arribo, atencion, tamanio, en_frente, mover_final


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
