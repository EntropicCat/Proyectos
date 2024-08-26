#Programe la función es_multiplo(n, m) que tome dos valores enteros como
#argumento y retorne True si n es múltiplo de m, esto es, si n = m * i para algún
#entero i, y False en caso contrario. Demuestre el correcto funcionamiento de la
#función es_multiplo invocándola a través de una aplicación de consola donde el
#usuario pueda ingresar datos y visualizar los resultados.

def es_multiplo(num1,num2):
    resultado = False
    aux = 0
    i = 0
    if num1 > num2:
        while aux <= num1:
            aux = 0
            i += 1
            aux = num2 * i
            if aux == num1:
                resultado = True
    return resultado    

#Código principal
print("Ingrese dos números para verificar si son multiplos")
n = int(input("Ingrese el primer numero: "))
m = int(input("Ingrese el segundo numero: "))

multiplo = es_multiplo(n,m)

if multiplo == True:
    print(n, " es multiplo de ", m)
else:
    print(n, " no es multiplo de ", m)




