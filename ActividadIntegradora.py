listaNumero = []

numeroUno = int (input("Ingrese el primer número: "))
listaNumero.append (numeroUno)
numeroDos = int (input("Ingrese el segundo número: "))
listaNumero.append (numeroDos)
numeroTres = int (input("Ingrese el tercer número: "))
listaNumero.append (numeroTres)
numeroCuatro = int (input("Ingrese el cuarto número: "))
listaNumero.append (numeroCuatro)
numeroCinco = int (input("Ingrese el quinto número: "))
listaNumero.append (numeroCinco)

print ("Los números introducidos por el usuario son:", listaNumero)

sumaParametros = sum(listaNumero)

print ("La suma total de los valores es: ",sumaParametros)

promedioLista = sumaParametros / 5

print ("El promedio de los números de la lista es: ", promedioLista)

funcionMaximo = max (listaNumero)

print ("El valor máximo de la lista es: ",funcionMaximo)

funcionMinimo = min (listaNumero)

print ("El valor mínimo de la lista es el: ", funcionMinimo)