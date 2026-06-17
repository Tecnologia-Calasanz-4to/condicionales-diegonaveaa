def matricula_valida(matricula):
    validacion= len(matricula) >= 3 and matricula[0:2].isalpha() and matricula[2:].isdigit()
    return validacion
def codigo_mision(matricula, anio):
    a="M-" + matricula[0:2].upper() + str(anio)
    return a
def energia_despegue(masa, velocidad):
    b= masa * velocidad ** 2
    return b

matricula=input("Ingresa la matricula")
anio=input("Ingresa el año")
masa=int(input("Ingresa la masa"))
velocidad=int(input("Ingresa la velocidad"))
a=matricula_valida(matricula)
b=codigo_mision(matricula, anio)
c=energia_despegue(masa, velocidad)
print(a,b,c)
