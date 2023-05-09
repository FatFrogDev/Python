#Leer 10 números y obtener su cubo a la cuarta
i=1
while i<=10:
    num = int(input('Ingresa el número para obtener su cubo a la cuarta \n'))
    cubo=num*num*num
    cuarta= num*num*num*num
    print('El cubo de ', num, ' es ', cubo, ' y la cuarta es: ', cubo)
    i+=1