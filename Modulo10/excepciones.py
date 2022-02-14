#Excepciones que son:
#las excepciones son errores que ocurren durante la ejecucion del programa. La sintaxis del codigo es correcta
#pero durante la ejecucion ha ocurrido "algo inesperado".
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede divir entre 0")
        return "Operacion erronea"
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))
        break
    except ValueError:
        print("los valores introducidos no son correctos. Intentalo de nuevo ")

operacion=input("Introduce la operacion a realizar (suma, resta, multiplica, divide): ")

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

print("Finalizacion y continuacion del programa ")