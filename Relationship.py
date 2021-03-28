# Relacion entre dos numeros 
def relacion(a, b):
    if a >b:
        print(1)
    if a <b:
        print(-1)    
    if a == b:
        print(0)

a = int(input('Escribe un numero: '))
b = int(input('Escribe un numero: '))
relacion(a, b)