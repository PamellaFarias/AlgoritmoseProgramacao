ordem=input().split()
linhas=int(ordem[0])
colunas=int(ordem[1])
matriz=[]
transposta=[]
for i in range(linhas):
    linha=input().split()
    matriz.append(linha)
for i in range(colunas):
    linhat=[]
    for j in range(linhas):
        linhat.append(matriz[j][i])
    transposta.append(linhat)  
print(transposta)
for i in range(colunas):
    for j in range(linhas):
        print((transposta[i][j]),end=" ")
    print()