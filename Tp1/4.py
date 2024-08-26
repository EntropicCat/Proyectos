#Escriba una función Python que tome como argumento una secuencia de números
#enteros y determine:
#a) La sumatoria
#b) El promedio.
#c) Si todos los números son diferentes entre sí, es decir, si todos los números de
#la lista son distintos.

def list_process(lista):
    sumatoria = sum(lista)
    long_list = len(lista)
    prom = sumatoria/long_list
    diff = False
    for n in lista:
        if lista.count(n)  > 1:
            diff = True
    print("Sumatoria: ", sumatoria)
    print("Promedio: ", prom)
    if diff == True:
        print("Hay numeros en la lista que se repiten")
    else:
        print("Todos los numeros de la lista son distintos")

#Algoritmo principal
lista_valores = [0,1,2,3,4,5,6,7,8,9]
list_process(lista_valores)

