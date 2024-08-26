#Programe la función min_max(data) que tome una secuencia de uno o más
#números y retorne el menor y el mayor de ellos en una tupla de dos posiciones de
#longitud. No utilizar la función min o max para solucionar este ejercicio. 

def min_max(data):
    min, max = 999999, -999999

    for n in data:
        if n < min:
            min = n
        elif n > max:
            max = n

    tupla = (min,max)
    return tupla

numeros_prueba = [14,5,98,25,78,10,69,45,87,209764]
tupla_res = min_max(numeros_prueba)
print(tupla_res)
