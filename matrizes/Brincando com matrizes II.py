matriz=[]
soma=0
delta=0
menor=1000
somandp=0
cont=0
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(input())
    matriz.append(linha)
for i in range(3):
    for j in range(3):
        if int(matriz[i][j])>-1:
            soma=soma+int(matriz[i][j])
            cont=cont+1
        if int(matriz[i][j])<menor:
            menor=int(matriz[i][j])
        if menor%2==0:
            delta=1
        else:
            delta=0
        if [i]!=[j]:
            somandp=somandp+int(matriz[i][j])
print("%.2f"%(soma/cont),menor,delta,somandp)
        