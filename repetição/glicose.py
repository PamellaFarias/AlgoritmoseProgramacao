soma=0
contador=0
while True:
    glicose=int(input())
    if glicose==0:
        break
    soma=soma+glicose
    contador=contador+1
if (soma/contador)<110:
    print("Glicose Normal")
elif (soma/contador)>=200:
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")