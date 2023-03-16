matriz=[]
traco=[]
soma=0
ordem=int(input())
for i in range(ordem):
    linha=input().split()
    matriz.append(linha)
print("tr(A) = ",end="")
for i in range(ordem):
    for j in range(ordem):
        if [i] == [j]:
            traco.append(matriz[i][j])
            soma=soma+float(matriz[i][j])
for i in range(ordem):
    if i<ordem-1:
        print("(%.2f) + "%(float(traco[i])),end="")
    else:
        print("(%.2f) = %.2f"%(float(traco[i]),soma))
    

        
            