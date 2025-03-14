###Variables en Python.
## Variables con números. 
a = 10
b = 5
c = a + b
print(c) #Primer ejemplo.

# Variables con strings.
nombreCompleto = "Jorge Ordoñez" #Definiendo una variable con camelCase.
nombre_completo = "Jorge Ordoñez" #Definiendo una variable con snake_case.
#La convención en Python es usar snake_case para definir variables.
print(nombre_completo) # Segundo ejemplo.

# Explicación: nombre = "Jorge Ordoñez" es una variable que almacena un string. "nombre =" es el nombre de la variable y "Jorge Ordoñez" es el valor de la variable. Una variable se declara, y cuando se lo asigna un valor se le está definiendo.

nombre = "Jorge Ordoñez"
nombre = "Arturo Gonzalez"
nombre = "Carlos Perez"
print(nombre) # Tercer ejemplo. Las variables pueden cambiar de valor.

numero = 10
numero += 5 #El simbolo += es un operador de asignación que suma el valor de la variable con el valor que se le asigna.
numero -= 5 #El simbolo -= es un operador de asignación que resta el valor de la variable con el valor que se le asigna.
numero *= 5 #El simbolo *= es un operador de asignación que multiplica el valor de la variable con el valor que se le asigna.
numero /= 5 #El simbolo /= es un operador de asignación que divide el valor de la variable con el valor que se le asigna.
print(numero) # Cuarto ejemplo. 

# Explicación: En el cuarto ejemplo se muestra como se pueden realizar operaciones con variables numéricas. En este caso se muestra como se puede sumar, restar, multiplicar y dividir una variable numérica.

## Concatenación de strings.
nombre = "Jorge"
bienvenida = "Hola " + nombre + ", Como estas?" #Se concatena el string "Hola" con el valor de la variable nombre y el string "Como estas?".
    #El operador + se usa para concatenar strings.
    #los espacios en blanco son importantes para que el texto se vea bien. No olvides ponerlos.
print(bienvenida) #Quinto ejemplo.

nombre = "Jorge"
bienvenida = f"Hola {nombre}, Como estas?" #Se usa la f antes de las comillas para concatenar strings. Esto se llama f-string.
    #Las f-string son una forma de concatenar strings de forma más sencilla.
    #Las f-string se usan para concatenar strings con variables, expresiones, funciones, métodos, operadores y otros strings.
del nombre #Se elimina la variable bienvenida.Es importante recordar que para eliminar una variable, se tiene que hacer antes de declararla.
print(bienvenida) #Sexto ejemplo.

## Operadores de pertenencia (in y not in) y de identidad.
nombre = "Jorge"
bienvenida = f"Hola {nombre}, Como estas?"
print("ola" in bienvenida) #El operador in se usa para verificar si un valor se encuentra en una variable.
#El resultado de la operación es un valor booleano.
nombre = "Jorge"
bienvenida = f"Hola {nombre}, Como estas?"
print("pedro" not in bienvenida) #El operador not in se usa para verificar si un valor no se encuentra en una variable.
#El resultado de la operación es un valor booleano.
bienvenida = f"Hola {nombre}, Como estas?"
print("hola" not in bienvenida)
#En este caso el resultado es False porque la palabra "hola" si se encuentra en la variable bienvenida. Python es sensible a mayúsculas y minúsculas (case-sensitive). 
