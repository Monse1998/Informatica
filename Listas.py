'''# Crear una lista
lista = ["david","ofe","lalo","hector"]
print(lista)
'''
lista2 = ["0.25",0.81,265]
print(lista2)
'''
lista3 = ["david","ofe",3,5.6,True,False,["monse",2.7,"miranda"]]
print(lista3)

lista4 = lista + lista3
print(lista4)

# Impresión de los valores de una lista
print(lista[-1])
# Impresión de un rango de valores en la lista
print(lista[0:2])		# Imprime un valor antes del valor indicado

# Para saber cuantos elemento tiene una lista
print(f"El número de elementos dentro de la lista 1 es de {len(lista)} elementos")
print(f"El número de elementos dentro de la lista 3 es de {len(lista3)} elementos")
print(f"El número de elementos dentro de la lista 4 es de {len(lista4)} elementos")

# Opciones para agregar nuevos elementos a una lista
listaone = [1,2,3,4,5]
numero = int(input(f"Dame un número: "))
listaone.append(numero)		#Lo agrega al final de la lista
print(listaone)

listatwo = ["angel","carmen","paola"]		# Agregar a Rafa
nombre = input(f"Dame el nombre a agragar: ")
listatwo.append(nombre)
print(listatwo)

# Colocar en una posición deseada un valor
listatree = [1,2,3,4,5]
# Posición, elemento
listatree.insert(2,3)
print(listatree)

listafour = ["Angel","Carmen","Paola"]
nombre = input(f"Dame el nombre a agragar: ")
posi = int(input(f"En que posición lo deseas agragar: "))
listafour.insert(posi,nombre)
print(listafour)
'''
# Como concatenar dos listas
lista2.extend(["Raul","Javier","Luis"])
print(lista2)
nombres = ["Joel","María","Carlos"]
lista2.extend(nombres)
print(lista2)