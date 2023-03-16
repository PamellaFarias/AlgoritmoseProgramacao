matriz=[]
k=int(input())
while k!=0:
    for i in range(4):
        linha=[]
        for j in range(4):
            linha.append(input())
        matriz.append(linha)
    matrizck=[]
    for i in range(4):
        linhack=[]
        for j in range(4):
            linhack.append(matriz[j][i])
        matrizck.append(linhack) 
    for i in range(4):
        for j in range(4):
            if [i]==[j]:
                (matrizck[i][j])=int(matriz[i][j])*k
    k=int(input())
for i in range(4):
    for j in range(4):
        print((matrizck[i][j]),end=" ")
    print()
