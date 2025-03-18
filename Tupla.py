# Una tupla es una lista que no pude agregar ni eliminar sus elementos

tupla = ("david","ofe","Tasha",[1,3,2],4,4.5)
print(tupla)
'''tupla.pop("david")				# No se puede eliminar nada de la tupla original
tupla.append("luis")				# No se puede agrapar nada a la tupla'''
print(tupla)

# Saber la posicion de uno de un elemento
nomb=input("que posicion deseas saber?")
posicion = tupla.index(nomb)
print(posicion)

#Convertir una tupla en una lista y viceversa
lista=list(tupla)
print(lista)
tupla2=tuple(lista)
print(tupla2)