n=int(input())
notas=[]
soma=0
maiores=0
menores=0
for i in range(n):
    notas.append(int(input()))
    soma=soma+notas[i]
media=soma/n
print("%.2f"%media)
for j in range(n):
    if (notas[j]) > 1.1*media:
        maiores=maiores+1
    elif(notas[j]) < 0.9*media:
        menores=menores+1
print(maiores)
print(menores)

