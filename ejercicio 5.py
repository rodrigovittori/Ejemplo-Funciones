#Ventajas: Si el código es demasiado largo p/ compartirlo por chat, puedo dividirlo en fn's

# [M5.L2] - Actividad Nº 4: "Los argumentos de la funcion (teoría)"

def sumar(a, b):
    print(a, "+", b, ":", (a+b))

#####################################

def restar(a, b):
    print(a, "-", b, ":", (a-b))

#####################################

def multiplicar(a, b):
    resultado = 0 # vble acumuladora
    for i in range(b):
        resultado += a
    print(str(a), "*", str(b), ":", resultado)

#####################################

def dividir(dividendo, divisor):
    print(str(dividendo), "/", str(divisor), ":", dividendo/divisor)

#####################################   
    
def dividir_enteros(dividendo, divisor):
    div_orig = dividendo # Guardo el valor para mostrarlo en el print
    cociente = 0 # resultado # vble contadora
    while(dividendo >= divisor):
        dividendo -= divisor
        cociente += 1
    dividendo = div_orig # Restauro valor original p/ el print
    print(str(dividendo), "/", str(divisor), "(solo entero) :", cociente)

#####################################   
    
def elevar(base, exponente):
    resultado = base
    for i in range(exponente - 1):
        resultado *= base
    print(str(base), " elevado a la ", str(exponente), ":", resultado)

#####################################   
# Programa

sumar(30, 50)
restar(80, 10)
multiplicar(3, 5)
dividir_enteros(13, 3)
dividir(13, 3)
elevar(2, 8)