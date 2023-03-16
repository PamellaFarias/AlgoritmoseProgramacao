n=int(input())
matriz=[]
matrizalt=[]
for i in range(n):
    linha=input().split()
    matriz.append(linha)
for i in range(n):
    linhaalt=[]
    for j in range(n):
        linhaalt.append(matriz[j][i])
    matrizalt.append(linhaalt)
for i in range(n):
    for j in range(n):
        if int(matrizalt[i][j])>0:
            print(matrizalt[i][j], end=" ")
        else:
            print(int(matrizalt[i][j])*2, end=" ")
    print()
        

