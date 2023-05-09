# Leer tres números diferentes e imprimir el número mayor de los tres.
num1 = int(input('ingrese el número 1\n'))
num2 = int(input('ingrese el número 2\n'))
num3 = int(input('ingrese el número 3\n'))

if num1>num2 and num1>num3:
    print('El número 1 es el mayor, tiene valor de: ', num1)
elif num2>num1 and num2>num3:
    print('El número 2 es el mayor, tiene valor de: ', num2)
elif num3>num1 and num3>num2:
     print('El número 3 es el mayor, tiene valor de: ', num3)
