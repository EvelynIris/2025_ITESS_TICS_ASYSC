#Materia: Analisis de senales y sistemas de comunicacion
#Maestro: Dr. Francisco Javier Montecillo Puente
#Periodo: SEPTIEMBRE-DICIEMBRE 2025
#Unidad 3
#Alumna: Evelyn Iris Hernandez Vigil
#suma, multiplicacion, division con doble diagonal, resta, modulo, exponente

#Imprimir un mensaje
print ("Hola mundo")

print ("NUMEROS a: 5, b:2")
a = 5
b = 2

#Suma
print("Suma: " + str(a+b)) #str convierte un dato en una cadena de texto

#Resta
print("Resta: " + str(a-b))

#Division
print("Divison: " + str(a/b))

#Division entera
print("Division entera: " + str(a // b))

#Modulo
print("Modulo " + str(a % b))

#Multiplicacion y suma
print("Multiplicacion y suma: " + str(5 * 3 + 2))

print("Potencias: " + str(5 ** 2))

ancho = 20
largo = 5 * 9
print("Largo * ancho: " +  str(ancho * largo))

impuesto = 12.5/100
precio = 100.50
print ("Precio * impuesto" + str(precio * impuesto))

print("CADENAS DE TEXTO")
print ('Huevos y pan')
print ('doesn\'t')
print ("doesn't")
print ('"Si," le dijo.')
print("\"Si,\" le dijo.")
print('"Isn\'t," she said.')

s = 'Primera linea. \nSegunda linea.'
print(s)
print(r'C:\algun\nombre') #\ son interpretados como caracteres especiales cuando se coloca la r

print("""\
Uso: algo [OPTIONS]
-h Muestra el mensaje de uso
-H nombrehost Nombre del host al cual conectarse
""") #Cadena con multiples lineas

print(3 * 'un' + 'ium') #lineas de texto concatenadas
print('Py' 'thon')
prefix = 'py'
print(prefix + 'thon') #Concatenar variables con un literal

texto = ('Poné muchas cadenas dentro de paréntesis '
'para que ellas sean unidas juntas.') #separa cadenas largas
print(texto)

#Rebanadas, permiten incluir sub cadenas
palabra = "Python"
print(palabra[0])  # Imprime 'P'
print(palabra[5])  # Imprime 'n'
print(palabra[-1]) # ultimo caracter
print(palabra[-2]) # penuntimo caracter
print(palabra[-6])

print(palabra[0:2])   # 'Py' desde el indice 0 hasta el 2 
print(palabra[:2])    # 'Py' desde el inicio hasta el indice 2
print(palabra[4:])    # 'on' desde el indice 4 hasta el final
print(palabra[:])     # 'Python' toda la cadena
#Puede dar error ya que las cadenas no pudene ser modificadas, si se necesita una cadena diferente se crea una nueva
print('J' + palabra[1:])
print(palabra[1:] + 'py')

#la funcion len devuelve la longitud de la cadena 
si = 'supercalifrastilisticoespialidoso'
print(len(si))

print("LISTAS")
cuadrados = {1, 4, 9, 16, 25}
print(cuadrados)
#Cadenas rebanadas
#print(cuadrados[-3:]) #Rebanadas que retornan a una nueva lista

cubos = [1, 8, 27, 65, 125]  # El cubo de 4 esta mal
print("Cubo de 4:", 4 ** 3)  # Verificaque sea 64

# Corrige el valor incorrecto
cubos[3] = 64
print("Cubos corregidos:", cubos)

# Se agregan nuevos
cubos.append(216)       # Cubo de 6
cubos.append(7 ** 3)    # Cubo de 7
print("Cubos extendidos:", cubos)

# Lista de letras
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Letras originales:", letras)

# Reemplazar algunos valores 
letras[2:5] = ['C', 'D', 'E']
print("Letras modificadas:", letras)

# Borrar esos valores
letras[2:5] = []
print("Letras tras borrar elementos:", letras)

# Vaciar toda la lista
letras[:] = []
print("Letras vacías:", letras)

# longitud de una lista
letras = ['a', 'b', 'c', 'd']
print("Longitud de letras:", len(letras)) 

# Lista aninada
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

print("SERIE DE FIBONACCI")
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

i = 256*256
print('El valor de i es ', i)

while b < 100:
    print(b, end=',') # end evita un salto de linea al final de la salida
    a, b = b, a + b

print(" ")
"""
print("SETENCIA IF") #elif es abreviacion del else if, sustituye la secuancia switch de otros lenguajes
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
    x = 0
    print("Negativo cambiado a cero")
elif x == 0:
    print("Cero")
elif x == 1:
    print("Simple")
else:
    print("Mas")
print(" ") """

print("SENTENCIA FOR")
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
    print(p, len(p))
print(" ")

print("FUNCION RANGE")  # genera progresiones aritmeticas
for i in range(5):
    print(i)


a = ['Mary', 'tenia', 'un', 'corderito']  # Itera sobre los índices de una secuencia

for i in range(len(a)):
    print(i, a[i])

list(range(5)) #crea listas a partir de iterables
print(" ")

print("SENTENCIAS BREAK, CONTINUE Y ELSE EN LAZOS")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, 'es un numero primo')

for n in range(2, 10):
    if n % 2 == 0:
        print("Encontre un numero par", n)
        continue
    print("Encontre un numero impar", n)
print(" ")

"""print("SENTENCIA PASS") # no hace nada, el programa no requiere ninguna accion
while True:
    pass """

print("FUNCIONES") # def define funciones, le sigue el nombre y la lista de parametros
def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()  # salto de lnea al final

def fib2(n):
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# Llamar a la funcion
f100 = fib2(100)

# Mostrar el resultado
print(f100)
print(" ")

print("ARGUMENTOS POR OMISION")
def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos -= 1
        if reintentos < 0:
            raise OSError('usuario duro')
        print(queja)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))  
print(f(2))  
print(f(3))  

print("PALABRAS CLAVE COMO ARGUMENTO")
def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nórdico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

#Llamadas
# 1 argumento posicional
loro(1000)

# 1 argumento nombrado
loro(tension=1000)

# 2 argumentos nombrados
loro(tension=1000000, accion='VOOOOOM')

# 2 argumentos nombrados en distinto orden
loro(accion='VOOOOOM', tension=1000000)

# 3 argumentos posicionales
loro('un millon', 'despojado de vida', 'saltar')

# Mezcla de posicional y nombrado (ojo con el nombre correcto)
loro('mil', estado='viendo crecer las flores desde abajo')

def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    
    for arg in argumentos:
        print(arg)
    
    print("-" * 40)
    
    claves = sorted(palabrasclaves.keys())
    for c in claves:
        print(c, ":", palabrasclaves[c])


ventadequeso(
    "Limburger",
    "Es muy liquido, sr.",
    "Realmente es muy muy liquido, sr.",
    cliente="Juan Garau",
    vendedor="Miguel Paez",
    puesto="Venta de Queso Argentino"
)
print(" ")

print("LISTA DE ARGUMENTOS ARBITRARIOS")
"""def concatenar(*args, sep="/"):
    return sep.join(args)
"""
print(" ")

print("DESEMPAQUETADO DE ARGUMENTOS")
print(list(range(3, 6)))  # [3, 4, 5]

# Desempaquetando desde una lista
args = [3, 6]
print(list(range(*args)))  # [3, 4, 5]

print("EXPRESIONES LAMBDA") #retoma la suma de sus dos argumentos
def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42)
print(f(0))  # 42
print(f(1))  # 43
