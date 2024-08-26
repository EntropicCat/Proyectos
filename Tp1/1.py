#Solicite al usuario el ingreso de un número entero entre 1 y 20 y muestre por
#pantalla las tablas de multiplicación del 1 al 10. 
num = int(input("Ingrese un número entero entre 1 y 20: "))

while num > 20 or num < 1:
    num = int(input("Ingrese un número entero entre 1 y 20: "))

for i in range(1,11):
    i = i*num
    print(i)
