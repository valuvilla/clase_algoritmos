

# VARIABLES ESTATICAS

num1 = 10
num2 = num1
num2 = num2 + 5

print(num1, num2)

a = input()
# VARIABLES DINAMICAS

vec1 = [1, 2, 3, 4]
vec2 = vec1
vec2[3] = 100

print(vec1, vec2)

class pelicula():

    def __init__(self):
        self.titulo, self.estudio, self.anio = '', '', ''

p = pelicula()
p.estudio

dato = ['titulo', 'estudio', 'anio']
dato[1]