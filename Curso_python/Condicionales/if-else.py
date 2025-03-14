# Descripción: Ejemplo de uso de condicionales if-else en Python

#if True:
    #accion
#if False:
    #accion
    
# Ejemplo.
contraseña_almacenada = "JorgeMaestro"
contraseña_escrita = '''JorgeMaestro'''

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESIÓN...")
    #Todo lo que este dentro de esta indentación se ejecutará si la condición es verdadera.
else:
    print("CONTRASEÑA INCORRECTA, INTENTE DE NUEVO.")
    #Todo lo que este dentro de esta indentación se ejecutará si la condición es falsa.
    
