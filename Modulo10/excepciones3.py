#lanzamiento de excepciones, instruccion raise, creacion de excepciones propias(para POO)

def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No es posible que tengas menos de 0")   
    ''' raise nos permite mandar un error en cierta parte del programa '''
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate..."

print(evaluaEdad(5))