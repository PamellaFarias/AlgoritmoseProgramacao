def maior(numero):
    maiorAB=((int(numero[0])+int(numero[1])+abs(int(numero[0])-int(numero[1]))))/2
    maiorABC=(int(maiorAB)+int(numero[2])+abs(int(maiorAB)-int(numero[2])))/2
    return(int(maiorABC))
numero=input().split()
print((maior(numero)),"eh o maior")