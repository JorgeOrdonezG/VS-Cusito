#Métodos con Strings.
cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"
#print(dir(dato)) # Nos muestra los métodos que podemos usar con cadenas. Es una función.

#Estructura: nombre = dato.metodo(parametros)
#Métodos que convierten cadenas.
mayusc = cadena1.upper() # Convierte la cadena a mayúsculas.

minusc = cadena1.lower() # Convierte la cadena a minúsculas.

primer_letra_mayusc = cadena1.capitalize() # Convierte la primera letra de la cadena a mayúscula. Pero con el resto de la cadena en minúsculas.

#Métodos de búsqueda.
busqueda_find = cadena1.find("5") # Nos devuelve la posición de la cadena que le pasamos como argumento. 
#En número de índice. -1 si no lo encuentra. #Recordar que es Case Sensitive.

busqueda_index = cadena1.index("Hola") # Nos devuelve la posición de la cadena que le pasamos como argumento. La diferencia con find es que si no lo encuentra, nos arroja un error (Exepción).


#Métodos de validación.
#Si es númerico nos devuelve True, si no False.
es_numerico = cadena1.isnumeric()

#Si es alfanumérico nos devuelve True, si no False.
es_alfanumerico = cadena1.isalpha()
#Arrojara False si el dato contiene espacios o caracteres especiales.

#Busqueda de coincidencias de una cadena dentro de otra cadena.
contar_coincidencias = cadena1.count("D") # Nos devuelve la cantidad de veces que se repite la cadena que le pasamos como argumento.
#Si no encuentra la cadena, nos devuelve 0. Recordar que es Case Sensitive, y toma en cuanta los espacios.

#Contamos la cantidad de caracteres de una cadena.
#len no es un método, es una función. Por lo tanto su estructura es diferente.
#nombre = len(dato)
contar_caracteres = len(cadena1)

#Verificamos si una cadena comienza con una cadena en específico.
empieza_con = cadena1.startswith("H") # Nos devuelve True si la cadena comienza con la cadena que le pasamos como argumento, si no False.
#Recordar que es Case Sensitive.

#Verificamos si una cadena termina con una cadena en específico.
termina_con = cadena1.endswith("Dalto") # Nos devuelve True si la cadena termina con la cadena que le pasamos como argumento, si no False.
#Recordar que es Case Sensitive.

#Reemplazamos una cadena por otra.
cadena_nueva = cadena1.replace(",", " ") # Reemplaza la cadena que le pasamos como primer argumento, por la cadena que le pasamos como segundo argumento.
# Estrucutra: nombre = cadena.replace("cadena a reemplazar", "cadena nueva")
#En caso de no encontrar la cadena, no arroja error, simplemente no hace nada.
cadena_nueva_2 = cadena_nueva.capitalize()

print(cadena_nueva)

# Los métodos son funciones especificas de un objeto.
