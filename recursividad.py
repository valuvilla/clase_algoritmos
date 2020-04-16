def suma_resta(num1, num2):
    return num1 + num2, num1 - num2

def nueva(vec):
    vec[0] = 101

def suma(num):
    num = num * 2

def factorialI(numero):
    factorial = 1
    for i in range(2, numero+1):
        factorial = factorial * i
    return factorial

def factorial(numero):
    if(numero == 1):
        return 1
    else:
        # 5! = 5 * 4!
        return numero * factorial(numero -1)

'''
print()
print(factorial(5))
print(factorialI(5))
'''


def fibonacciI(numero):
    fib1 = 0
    fib2 = 1
    for i in range(2, numero+1):
        aux = fib1 + fib2
        fib1 = fib2
        fib2 = aux
    return aux

def fibonacci(numero):
    if(numero==0 or numero==1):
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)

def sumaR(numero):
    if(numero==0):
        return numero
    else:
        return numero + sumaR(numero-1)

def producto(numero1, numero2):
    if(numero2==1):
        return numero1
    else:
        return numero1 + producto(numero1, numero2-1)

def potencia(base, exponente):
    pass


def bbin(vector, buscado, primero, ultimo):
    if(primero <= ultimo):
        med = (primero + ultimo) // 2
        if(vector[med] == buscado):
            return med
        elif(vector[med] > buscado):
            return bbin(vector, buscado, primero, med-1)
        else:
            return bbin(vector, buscado, med+1, ultimo)
    else:
        return -1

# Quicksort
def quicksort(vector, primero, ultimo):
    if(primero<ultimo):
        pivot = ultimo
        izq = primero
        der = ultimo-1
        while(izq < der):
            while(vector[izq] < vector[pivot]):
                izq += 1
            
            while(vector[der] > vector[pivot]):
                der -= 1

            if(izq < der):
                vector[izq], vector[der] = vector[der], vector[izq]

        if(vector[izq]>vector[pivot]):
            vector[izq], vector[pivot] = vector[pivot], vector[izq]

        quicksort(vector, primero, izq-1)
        quicksort(vector, izq+1, ultimo)

def logaritmo(base, numero):
    if(base == numero):
        return 1
    else:
        return 1 + logaritmo(base, numero/base)


def sucecion24(termino):
    if(termino==1):
        return 5.25
    else:
        return sucecion24(termino-1) * 4



'''
for i in range (10,0,-1):
    print(sucecion24(i))
'''


def binario(numero):
    if(numero <= 1):
        return str(numero)
    else:
        return binario(numero//2) + str(numero % 2) 


#print(binario(8))

matriz = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]


print("matriz")
'''
for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j])
'''
def barrido_matriz(mat, i, j):
    if(i<len(mat) and j<len(mat[i])):
        print(mat[i][j])
        if(j == len(mat[i])-1):
            i += 1
            j = -1
        barrido_matriz(mat, i, j+1)

barrido_matriz(matriz, 0, 0)

print("fin")
vector = [1,2,3,4,5,6,7,8]

def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

# barrido(vector)

vec = [['coordenadas', 'blaster principal', False],
       ['coordenadas', 'blaster secundario', True],
       ['coordenadas', 'cañon', True],
       ['coordenadas', 'blaster principal', False]]

def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

print("total de naves derribadas", contar_naves(vec))

matriz = [[0,0,0,0,0],
          [1,0,1,0,1],
          [1,0,0,0,1],
          [1,0,1,1,1],
          [1,0,0,0,2]
          ]


def mcd(m, n):
    """Cálculo del máximo comun divisor."""
    if(m % n == 0):
        return n
    else:
        return mcd(n, m % n)


def mcm(m, n):
    """Cálculo del mínimo comun multiplo."""
    if(n % m == 0):
        return n
    else:
        return mcm(n, m * n)