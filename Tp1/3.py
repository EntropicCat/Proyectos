#Escriba un programa que exija al usuario el ingreso de:
#a) 2 números enteros y determine el mayor.
#b) 3 números enteros y determine el mayor.
#c) N números enteros y determine el mayor (no usar colecciones).

loop = 0
while loop < 3:
    fin = False
    mayor = 0
    i = 0
    loop += 1
    match loop:
        case 1:
            print("Ingrese dos numeros para determinar el mayor")
        case 2:
            print("Ingrese tres numeros para determinar el mayor")
        case 3:
            print("Ingrese cualquier cantidad de numeros para determinar el mayor")
            print("Para terminar ingrese 0")
    while i <= loop and fin == False :
        num = int(input("Ingrese el numero: "))
        if num > mayor:
            mayor = num
        if loop == 1 or loop == 2:
            i += 1
        else:
            if num == 0:
                fin = True
    mayor = str(mayor)
    print(mayor + " es el numero mayor")
    print()
    