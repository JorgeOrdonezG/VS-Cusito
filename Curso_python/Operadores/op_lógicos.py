#And
Resultado = True & True #True
Resultado2 = False & True #False
Resultado3 = True & False #False
Resultado4 = False & False #False
#Para que el resultado sea True, ambos valores deben ser True.

#Or
Resultado5 = True | True #True
Resultado6 = False | True #True
Resultado7 = True | False #True
Resultado8 = False | False #False
#Para que el resultado sea False, ambos valores deben ser False, con que una sea True, el resultado será True.

#Not
Resultado9 = not True #False
Resultado10 = not False #True
#El operador not invierte el valor de la variable.

print(Resultado)