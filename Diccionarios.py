# Crear un diccionario
diccionario = {}
diccionario = {1:"lapiz",2:"plumas", 3:"cajas"}
print(diccionario)
# Para mostrar un valor especifíco
print(diccionario[2])
    
while True:
    valor = input("Dame el valor que quieres encontrar (clave o valor): ")

    # Verificamos si el valor es un número entero y si está en las claves del diccionario
    if valor.isdigit():
        valor = int(valor)
        if valor in diccionario:
            print(f"Valor encontrado: {diccionario[valor]}")
        else:
            print("La clave no existe en el diccionario.")
    # Si no es un número, asumimos que es un valor y verificamos si está en el diccionario
    else:
        encontrado = False
        for clave, val in diccionario.items():
            if val.lower() == valor.lower():  # Comparación insensible a mayúsculas
                print(f"Valor encontrado: {val} para la clave {clave}")
                encontrado = True
                break
        
        if not encontrado:
            print("El valor no se encuentra en el diccionario.")
 
 
 
 
'''#para agragar valor al diccionario
diccionario[4]="gomas"
print(diccionario)'''