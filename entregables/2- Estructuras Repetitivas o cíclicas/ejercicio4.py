#Diseñe un diagrama que lea los 2,500,000 votos otorgados a los 3 candidatos a
#gobernador e imprima el número del candidato ganador y su cantidad de votos.
cant_votos=3
cand_1=0
cand_2=0
cand_3=0
for i in range(cant_votos):
    print(f'Digita 1,2 o 3 para votar para el candidato correspondiente al mismo número\n')
    voto=int(input('Ingresa por quién vas a votar\n'))
    if voto==1:
        cand_1+=1
    elif voto==2:
        cand_2+=1
    elif voto==3:
        cand_3+=1
    else:
        print('Por digitar el número mal, tu voto será anulado')
if cand_1>cand_2 and cand_1>cand_3:
    print(f'El candidato 1 ganó con {cand_1} votos')
elif cand_2>cand_1 and cand_2>cand_3:
    print(f'El candidato 2 ganó con {cand_2} votos')
elif cand_3>cand_1 and cand_3>cand_2:
    print(f'El candidato 3 ganó con {cand_3} votos')
elif cand_1 == cand_2 and cand_1==cand_3:
    print(f'Ha ocurrido un empate')
else:
    print('Error')