N=int(input())
matriz=[]
matrizdp=[]
matrizds=[]
inicial=1
contadord=0
contadors=0
contpd=0
contps=0
for i in range(N):
    linha=[]
    for j in range(N):
        linha.append(inicial)
        inicial=inicial+1
    matriz.append(linha)
for i in range(N):
    linhadp=[]
    for j in range(N):
        linhadp.append(matriz[i][j])
    matrizdp.append(linhadp)
for i in range(N):
    for j in range(N):
        if [i]!=[j]:
            if contadord < N:
                if i==0:
                    matrizdp[i][j]=""
                if i>0:
                    matrizdp[i][j]=""
    contadord=contadord+1
for i in range(N):
    linhads=[]
    for j in range(N):
        linhads.append(matriz[i][j])
    matrizds.append(linhads)
for i in range(N):
    for j in range(N):
        if i+j !=N-1:
            if contadors < N:
                if i==0:
                    matrizds[i][j]=""
                if i>0:
                    matrizds[i][j]=""

    contadors=contadors+1
print("Matriz:")
for i in range(N):
    for j in range(N):
            print(" ",matriz[i][j],end="")
    print()
print()
print("Diagonal Principal:")
for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            print(" ",matrizdp[i][j],end="")
        if i>0 and j< N-1:
            if matrizdp[i][j] =="":
                print("  ",matrizdp[i][j],end="")
            else:
                print(" ",matrizdp[i][j],end="")
                break
        if i>0 and j== N-1:
            if matrizdp[i][j] =="":
                print("  ",matrizdp[i][j],end=" ")
            else:
                print(" ",matrizdp[i][j],end="")
    contpd=contpd+1
    print()
print()
print("Diagonal Secundaria:")
for i in range(N):
    for j in range(N):
        if i==N-1:
            print(" ",matrizds[i][j], end="")
            break
        if i==0 and j ==N-1:
            print(" ",matrizds[i][j], end="")
        if i==0 and j <N-1:
            print(" ",matrizds[i][j], end=" ")
        if 0<i<N-1:
            if matrizds[i][j] =="":
                print("  ",matrizds[i][j],end=" ")
            else:
                print("",matrizds[i][j],end="")
                break
    print()