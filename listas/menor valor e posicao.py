array=[]
tamanho=int(input())
array=input().split()
menor_valor=int(array[0])
posicao=0
for i in range(1,tamanho):
    if int(array[i]) < int(menor_valor):
        menor_valor=int(array[i])
        posicao=i
print("Menor valor:",menor_valor)
print("Posicao:",posicao)
