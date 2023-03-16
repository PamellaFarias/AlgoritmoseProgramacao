ordem=input().split()
linhas=int(ordem[0])
colunas=int(ordem[1])
matriz=[]
diagonalp=0
diagonals=0
menor0=0
maior0=0
for i in range(linhas):
    linha=[]
    for j in range(colunas):
        linha.append(input())
    matriz.append(linha)
for i in range(linhas):
    for j in range(colunas):
        if [i]==[j]:
            diagonalp=diagonalp + int(matriz[i][j])
        if i+j == 2:
            diagonals=diagonals + int(matriz[i][j])
        if int(matriz[i][j]) < 0:
            menor0=menor0+1
        if int(matriz[i][j]) > 0:
            maior0=maior0+1
print("Matriz formada:")
for i in range(linhas):
    for j in range(colunas):
        if j<colunas-1:
            print(matriz[i][j],end=" ")
        else:
            print(matriz[i][j],end="")
    print()
if linhas==colunas:
    print("A diagonal principal e secundaria tem valor(es)",diagonalp,"e",diagonals,"respectivamente.")
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")
print("A matriz possui",menor0,"numero(s) menor(es) que zero.")
print("A matriz possui",maior0,"numero(s) maior(es) que zero.")