def divide():
    while True:
        try:
            op1=float(input("Digita un primer numero: "))
            op2=float(input("Digita un segundo numero: "))
            print("la division es: " + str(op1/op2))
            break
        except ValueError:
            print("El valor introducido es erroneo")
        except ZeroDivisionError:
            print("NO se puede divider entre 0!")

    ''' la sentencia finally es para que se ejecute de afuerzas  '''
    ''' finally: '''
    print("calculo finalizado")

divide()

''' 
try:
    something 
except:
    si no se especifica el error solo se va ahi el problema, aunque no 
    se da cuenta el usuario que estuvo mal en el bloque de codigo el programa no se va a caer
    '''
