s=input()
l=0
maior=""
while s!="0":
    lista=s.split()
    for i in range(len(lista)):
        if i ==len(lista)-1:
            print(len(lista[i]))
        else:
            print(len(lista[i]), end="-")
        if len(maior)<= len(lista[i]):
            maior=lista[i]
    s=input()
print("Maior palavra:", maior)
        
            
            
    