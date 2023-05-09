#Leer 20 números e imprimir: cuantos son positivos, cuantos son negativos y cuantos neutros 
i=1
posi=0
neg=0
neu=0
while i<=20:
    num=int(input('Ingresa un número \n'))
    if num>0:
        posi+=1
    elif num==0:
        neu+=1
    elif num<0:
        neg+=1
    i+=1
print(f'En los {i} números digitdos hay:  {posi} número positivos {neu} número neutros y {neg} números negativos')