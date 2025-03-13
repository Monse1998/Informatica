# Buscar si existe un elemento en una lista
lista = ["Monse","Chamoy","Sebas","Tarito","Tarito","Monse"]

'''
print ("Chamoy" in lista)
nombre=input("Que nombre buscas: ")
if nombre in lista:
    print (f"El nombre {nombre} si esta en la lista")
else:
    print (f"El nombre {nombre} no esta en la lista")

# Para obtener la posición o índice de un elemento en la lista
print (lista.index("Chamoy"))
pos = input ("De que nombre deseas conocer la posición: ")
if pos in lista:
    print(lista.index(pos))
else:
    print(f"El nombre no es valido: ")

# Contas cuantas veces esta repetido un elemento en la lista
print(lista.count("Tarito"))
cuantas = input("Nombre de quien quieres contar: ")
print(f"El nombre se repite {lista.count(cuantas)} veces")

# Como reemplazar un elemento en la lista
print(lista)
posi = input("")
nombre = input(f"Dame el nombre 1: ")
lista[0] = nombre
nombre = input(f"Dame el nombre 2: ")
lista[1]= nombre
print(lista)
while True:
    buscar = input(f"Dame el elemento a buscar: ")
    if buscar in lista:
        remp = input(f"Valor encontrado, ¿Por cual elemento deseas remplazarlo? ")
        lista[lista.index(buscar)]=remp
        print(f"Lista actualizada queda: {lista}")
        break
    else:
          print("El valor no se encuentra en la lista")'''

# Para borrar dattos de una lista
lista.pop()			#Eliminar el último elemento
lista.pop(1)
print(lista)
lista.clear()
print(lista)