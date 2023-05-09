    # Leer 2 números; si son iguales que los multiplique
# si el primero es mayor que el segundo que los reste, y si no que los sume
num1 = int(input('Ingresa el valor del número 1 \n'))
num2 = int(input('Ingresa el valor del número 2 \n'))
if num1==num2:
    print('La mutliplicación de ', num1, ' y', num2, ' es ', (num1*num2))
elif num1>num2:
     print('La resta de ', num1, ' y', num2, ' es ', (num1-num2))
else:
      print('La suma de ', num1, ' y', num2, ' es ', (num1+num2))

