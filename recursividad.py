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


print()
print(factorial(5))
print(factorialI(5))


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