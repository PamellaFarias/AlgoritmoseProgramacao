numeros=[]
soma=0
for i in range (10):
    nums=int(input())
    numeros.append(nums)
x=int(input())
for j in range(10):
    if (numeros[j])==x:
        soma=soma+1
print(soma)
