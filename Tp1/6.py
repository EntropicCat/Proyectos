#Escriba un programa Python que solicite al usuario el nombre de cada país del
#continente, su nombre, superficie y cantidad de habitantes. Almacene estos datos
#en una lista de elementos de tipo diccionario donde cada entrada tenga las
#componentes (pais, superficie y habitantes). A continuación cumplimente los
#siguiente incisos:
#a) Totalizar la cantidad de habitantes.
#b) Superficie total.
#c) Obtener el promedio de habitantes.
#d) Densidad poblacional de cada país.

continente = {"Pais" : [],
              "Superficie" : [],
              "Habitantes" : [] }

print("Ingrese los datos correspondientes. Pulse <F> para terminar el ingreso.")
pais = input("Ingrese nombre del pais: ")
while pais != "F":
    superficie = float(input("Ingrese la superficie del pais: "))
    habitantes = int(input("Ingrese la cantidad de habitantes: "))
    continente["Pais"].append(pais)
    continente["Superficie"].append(superficie)
    continente["Habitantes"].append(habitantes)
    print()
    pais = input("Ingrese nombre del pais: ")

tot_hab = sum(continente["Habitantes"])
tot_sup = sum(continente["Superficie"])
aux = len(continente)-1
prom_hab = tot_hab/aux
print("Total habitantes: ",tot_hab)
print("Total superficie: ",tot_sup)
print("Promedio habitantes ",prom_hab)
print()


for n in range(0,aux):
    densidad = float(continente["Habitantes"][n]/continente["Superficie"][n])
    print(continente["Pais"][n], " tiene una densidad poblacional de: ",densidad)
    print()

