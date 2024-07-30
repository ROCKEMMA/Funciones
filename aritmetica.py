# @sumar
# n1, solicita un numero
# n2, solicita otro número
# return, la suma de los dos números

def sumar(n1,n2):
    return n1+n2

def restar(n1,n2):
    return n1-n2

def dividir(n1,n2):
    return n1/n2

def multiplicar(n1,n2):
    return n1*n2


def operaciones(nombre,n1,n2):
    print(nombre)
    print(15*"-")
    print("Suma :",sumar(n1,n2))
    print("Resta :", restar(n1,n2))
    print("división : ", dividir(n1,n2))
    print("Multiplicación :",multiplicar(n1,n2))
    print(15*"-")


operaciones("Beyla",10,5)

def datos(nombre,edad):
    print("Nombre",nombre)
    print("Edad",edad)

datos("Jossue",30)