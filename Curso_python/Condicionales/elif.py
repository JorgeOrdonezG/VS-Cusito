ingreso_mensual = 72000
gasto_mensual = 8000

# If anidado y else if:

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("Bien pa, estás bien")
    elif ingreso_mensual - gasto_mensual > 0:
        print("y pa, estás gastando una banda, a ver si te alcanza.")
    else:
        print("Estás en deficit.")

elif ingreso_mensual > 1000:
    print("Estás bien económicamente en Latinoamérica.")

elif ingreso_mensual > 500:
    print("Estás bien económicamente en México.")
    
elif ingreso_mensual > 200:
    print("Estás bien económicamente en Venezuela.")
    
else:
    print("Eres pobre.")