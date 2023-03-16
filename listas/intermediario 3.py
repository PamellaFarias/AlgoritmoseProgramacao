numeros=[]
for i in range(3):
    nums=int(input())
    numeros.append(nums)
if (numeros[0])>(numeros[1]) and (numeros[0])>(numeros[2]):
    if numeros[1] > numeros[2]:
        print(numeros[1])
    else:
        print(numeros[2])
elif (numeros[1])>(numeros[0]) and (numeros[1])>(numeros[2]):
    if numeros[0] > numeros[2]:
        print(numeros[0])
    else:
        print(numeros[2])
else:
    if numeros[0] > numeros[1]:
        print(numeros[0])
    else:
         print(numeros[1])
        
    
