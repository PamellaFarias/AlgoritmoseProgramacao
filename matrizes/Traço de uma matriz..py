n=int(input())
m=int(input())
matriz=[]
traco=0
d=0
for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(input())
    matriz.append(linha)
if n != m:
    print("A matriz nao possui traco")
    for i in range(n):
        for j in range(m):
            if j<m-1:
                print((matriz[i][j]), end=" ")
            else:
                print((matriz[i][j]), end="")
        print()
else:
    for i in range(n):
        for j in range(m):
            if [i]==[j]:
                traco=traco+int(matriz[i][j])
            if i+j == n-1:
                d=d+int(matriz[i][j])
    print(traco)
    print(d)
    for i in range(n):
        for j in range(m):
            if j<m-1:
                print((matriz[i][j]), end=" ")
            else:
                print((matriz[i][j]), end="")
        print()