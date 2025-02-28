try : 
    c = input ('¿Temperature in C°?')
    f = int(c) * 9 / 5 + 32    
    
    print ('The temperature in F° is:' , f )

except ValueError:
    print('Ingrese un valor númerico, por favor.')