try:
    score = float(input ('¿Score?'))
    
    if score >= 0.9 :
        print ('Grade A')
    elif score >= 0.8 :
        print ('Grade B')
    elif score >= 0.7 :
        print ('Grade C')
    elif score >= 0.6 :
        print ('Grade D')
    elif score < 0.6 :
        print ('Grade F')
except ValueError:
    print ('Bad Score')