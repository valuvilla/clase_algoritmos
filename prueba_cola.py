
from tda_cola import Cola, cola_llena, cola_vacia, arribo, atencion, tamanio


c = Cola()
caux = Cola()

while not cola_llena(c):
    dato = int(input("ingrese un número"))
    arribo(c, dato)

while not cola_vacia(c):
    x = atencion(c)
    if(x % 2 == 0):
        arribo(caux, x)

while not cola_vacia(caux):
    x = atencion(caux)
    print(x)
