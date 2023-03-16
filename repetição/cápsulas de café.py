soma=0
for i in range(7):
    quantidade=int(input())
    tam=input()
    if tam=="g" or tam=="G":
        unidades=16
    else:
        unidades=10
    soma=soma+quantidade*unidades
print(soma)
print(int((soma*2)/7))

    

    

        

