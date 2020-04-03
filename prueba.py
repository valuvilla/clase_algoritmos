def horse_problem(cantidad_movimineto):
    """Calcula cantiad de movimientos de caballo de ajedrez en teclado tel."""
    teclado = {'0': ['4', '6'], '1': ['6', '8'], '2': ['7', '9'],
               '3': ['4', '8'], '4': ['0', '3', '9'], '6': ['0', '1', '7'],
               '7': ['2', '6'], '8': ['1', '3'], '9': ['2', '4']}
    total = 0
    for i in range(0, 10):
        if (i != 5):
            lista = teclado[str(i)]
            for j in range(1, cantidad_movimineto):
                aux = []
                for elemento in lista:
                    aux += teclado[elemento]
                lista = aux
            total = total + len(lista)
    return total


print("cantidad de movimientos", horse_problem(4))

saltos= 3

a=2
b=3
c=2
d=2

for i in range(saltos):
    total= 4*a+2*(b+c)+d
    ax=a
    bx=b
    cx=c
    a=bx+cx
    b=2*ax+d
    c=2*ax
    d=2*bx

print(total)

def pieza(clave):
    res = 0
    dosmov = 2
    tresmov = 3
    if clave == 1:
        res = (dosmov * 7) + (tresmov * 2)
    elif clave == 2:
        res = (dosmov * 14) + (tresmov * 6)
    elif clave == 3:
        res = (dosmov * 28) + (tresmov * 16)
    elif clave == 4:
        res = (dosmov * 56) + (tresmov * 43)
    elif clave == 5:
        res = (dosmov * 112) + (tresmov * 162)
    elif clave == 8:
        res = (dosmov * 896) + (tresmov * 4374)
    elif clave == 10:
        res = (dosmov * 3584) + (tresmov * 39366)
    elif clave == 12:
        res = (dosmov * 14336) + (tresmov * 354294)
    elif clave == 15:
        res = (dosmov * 114688) + (tresmov * 9565938)
    else:
        return 0
    return res


movfinal = pieza(4)
print(movfinal)