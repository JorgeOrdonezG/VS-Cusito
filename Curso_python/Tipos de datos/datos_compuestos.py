#Datos que pueden contener otros datos

#Listas
lista = ["Jorge Ordoñez", "Soy Jorge", True, 1.80] #Las listas se definen con corchetes.
print("Ejemplo de lista:")
print(lista) #['Jorge Ordoñez', 'Soy Jorge', True, 1.8]
print(lista[0]) #Jorge Ordoñez, sobre mencionar que las listas empiezan en 0. 
#Índice es la posicion de un elemento en la lista, elemento es el valor que se encuentra en la lista. Por tanto, el elemento 0 es "Jorge Ordoñez".

lista[3] = "Maquinola" #Cambiar el valor de un elemento en la lista.
print(lista[3]) #Maquinola.

#Tuplas
tupla = ("Jorge Ordoñez", "Soy Jorge", True, 1.80) #Las tuplas se definen con paréntesis.
print("Ejemplo de tupla:")
print(tupla) #('Jorge Ordoñez', 'Soy Jorge', True, 1.8).
print(tupla[0]) #Jorge Ordoñez, al igual que las listas, las tuplas empiezan en 0. Y a pesar de que se crean con pqaréntesis, se acceden con corchetes.
#tupla[3] = "Maquinola" #Error, no se puede modificar una tupla.
#Las tuplas son inmutables, es decir, no se pueden modificar una vez creadas.

#Creando un conjunto (set)

conjunto = {"Jorge Ordoñez", "Soy Jorge", True, 1.80, "Soy Jorge"} #Los conjuntos se definen con llaves.
print("Ejemplo de conjunto:")
print(conjunto) #{True, 1.8, 'Soy Jorge', 'Jorge Ordoñez'} #Los conjuntos no tienen orden, por lo que no se puede acceder a un elemento por su índice.
#conjunto[1] = "Pedrín" #Error, no se puede modificar un conjunto.
#Al igual que las tuplas, los conjuntos son inmutables.
#conjunto = {"Jajaja maquina te jodí"} #Se puede modificar el conjunto, pero no los elementos del conjunto.
#tupla = ("Jajaja maquina te jodí") #Se puede modificar la tupla, pero no los elementos de la tupla.
#print(conjunto[1]) #Error, no se puede acceder a un elemento por su índice.
#print(conjunto) #{'Jajaja maquina te jodí'}.

#Las listas y tuplas pueden mostrar elementos repetidos, pero los conjuntos no. Los conjuntos no tienen orden, por lo que no se puede acceder a un elemento por su índice.

#Diccionarios, la estructura es key-value. Si tiene mas de una clave, se separan por comas. El del final no lleva coma.
diccionario = {
    "nombre": "Jorge Ordoñez",
    "canal": "Soy Jorge",
    "esta_emocionado": True,
    "altura": 1.80,
    "dato_duplicado": "Soy Jorge"
} #Los diccionarios se definen con llaves y dos puntos.
#"nombre": "Jorge Ordoñez", es un par key-value, donde "nombre" es la clave y "Jorge Ordoñez" es el valor.
#Las claves de un diccionario deben ser únicas, es decir, no pueden haber dos claves iguales.
print("Ejemplo de diccionario:")
print(diccionario["nombre"]) #Jorge Ordoñez, se accede a un elemento del diccionario por su clave.