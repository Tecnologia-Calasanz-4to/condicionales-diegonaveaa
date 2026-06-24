def matricula_valida(matricula):
    if len(matricula) >= 3 and matricula[0:2].isalpha() and matricula[2:].isdigit():
        valor = True
    else:
        valor = False
    return valor
def codigo_mision(matricula, anio):
    a= ("M-") + matricula[0:2].upper() + str(anio)
    return a
def energia_despegue(masa, velocidad):
    b= masa * velocidad ** 2
    return b

def consumo_base(distancia, consumo_km):
    consumo= distancia * consumo_km
    return consumo
def hay_turbo(es_nave_nueva, velocidad):
    if es_nave_nueva or velocidad >= 1000:
        valorr = True
    else:
        valorr = False
    return valorr
def consumo_total(distancia, consumo_km, turbo):
    if hay_turbo(es_nave_nueva, velocidad):
       devolver=consumo_base(distancia,consumo_km)* 2
    else:
        devolver=consumo_base(distancia, consumo_km)
    return devolver

def nivel_combustible(consumo_km, maximo):
    nivel=   consumo_km / maximo * 100
    return nivel

def estado_tanque(porcentaje):
    if porcentaje <=15:
        return "CRITICO"
    elif porcentaje<=40:
        return "BAJO"
    elif porcentaje<=75:
        return "OK"
    else:
        return "LLENO"
def dias_y_horas(horas):
    dias= horas// 24
    horasres=horas % 24
    return dias,horasres




matricula=input("Ingresa la matricula")
anio=input("Ingresa el año")
masa=int(input("Ingresa la masa"))
velocidad=int(input("Ingresa la velocidad"))
a=matricula_valida(matricula)
b=codigo_mision(matricula, anio)
c=energia_despegue(masa, velocidad)
print(a,b,c)

distancia= int(input("Ingresá la distancia"))
consumo_km= int(input("Ingresá el combustible"))
es_nave_nueva=velocidad

d=consumo_base(distancia, consumo_km)
turbo=hay_turbo(es_nave_nueva, velocidad)
f=consumo_total(distancia, consumo_km, turbo)
maximo=10000
porcentaje= nivel_combustible(consumo_km, maximo)
nivel= estado_tanque(porcentaje)
horas= distancia//velocidad
diego=dias_y_horas(horas)
print (nivel, diego)
