try:
    horas = float(input('¿Horas trabajadas?'))
    ratio = float(input('¿Ratio?'))

    if horas > 40:
        pago = (40 * ratio) + ((horas - 40) * ratio * 1.5)
    else: 
        pago = horas * ratio
        
    print ('A pagar:' , pago)
    
except ValueError:
    print ('Ingrese un valor númerico.') 
    
