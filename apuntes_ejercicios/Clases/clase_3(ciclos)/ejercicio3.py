#Calcular e imprimir la tabla de multiplicar de un número cualquiera
#imprimir el multiplicando, multiplicador y prodcto
i=1
num=int(input('Ingrese el número para sacar su tabla de multipllicar\n'))
while i<=10:
    resultado=num*i
    print(f'{num}*{i} es igual a: {resultado}')
    i+=1