'''Ingreso de los números a sumar'''

listaNumeros = []

for i in range(5):
    x = int(input('Ingrese un número: '))
    listaNumeros.append(x)
print('Números Ingresados:', listaNumeros)

'''SUMA'''

def calc_suma():
    suma = 0
    for i in range(5):
        suma += listaNumeros[i]
    return suma

print('suma:',calc_suma())

'''Cálculo del Promedio. Usando función len()'''

def calc_prom():
    suma = 0
    cant=len(listaNumeros)
    for i in range(cant):
        suma += listaNumeros[i]
        promedio = suma / cant
    return promedio

print('Promedio:',calc_prom())

'''Búsqueda del mayor num '''
def calc_may():
    cant=len(listaNumeros)
    for i in range(cant):
        mayor= max(listaNumeros)
    return mayor
print('Mayor:',calc_may())

'''Búsqueda del menor num '''
def calc_menor():
    cant=len(listaNumeros)
    for i in range(cant):
        menor= min(listaNumeros)
    return menor
print('Mayor:',calc_menor())
