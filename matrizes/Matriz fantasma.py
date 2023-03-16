n=int(input())
matriz=[]
inicial=1
contador=0
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(inicial)
        inicial=inicial+1
        matriz.append(linha)
    if inicial==n:
        inicial=0
for i in range(n):
    for j in range(n):
        if contador < n:
            if i>0 and j==0:
                matriz[i][j]=" "
            if i>0 and j<contador:
                matriz[i][j]=" "
            if j<n-1:
                print((matriz[i][j]), end=" ")
            else:
                print((matriz[i][j]), end="")
    contador=contador+1
    print()
    