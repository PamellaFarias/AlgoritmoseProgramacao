aprovados=0
while True:
    certas_portugues=int(input())
    if certas_portugues<0:
        break;
    certas_matematica=int(input())
    nota_redacao=float(input())
    if ((certas_portugues/50)>=0.8 and (certas_matematica/35)>=0.6 and nota_redacao>=7.0):
        aprovados=aprovados+1
print(aprovados)
