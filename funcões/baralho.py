def pontuacao(paes,willy):
    vencedor=0
    menorp=int(paes[0])
    menorw=int(willy[0])
    pontuacaop=0
    pontuacaow=0
    contadorp=1
    contadorw=1
    contador2p=1
    contador2w=1
    maiorp=int(paes[0])
    maiorw=int(willy[0])
    if int(paes[0])+1== int(paes[1]) and int(paes[1])+1== int(paes[2]):
        pontuacaop=pontuacaop+int(paes[0])
    if int(willy[0])+1== int(willy[1]) and int(willy[1])+1== int(willy[2]):
        pontuacaow=pontuacaow+int(willy[0])
    if int(paes[0])== int(paes[1]) == int(paes[2]):
        pontuacaop=pontuacaop+int(paes[0])    
    if int(willy[0])== int(willy[1]) == int(willy[2]):
        pontuacaow=pontuacaow+int(willy[0])
    for i in range(1,3):
        if int(paes[i])<menorp:
            menorp=int(paes[i])
        if int(paes[i])==menorp:
            contadorp=contadorp+1
    if contadorp==2:
        pontuacaop=pontuacaop+int(menorp/2)
    for i in range(1,3):
        if int(willy[i])<menorw:
            menorw=int(willy[i])
        if int(willy[i])==int(menorw):
            contadorw=contadorw+1
    if contadorw==2:
        pontuacaow=pontuacaow+int(menorw/2)
    for i in range(1,3):
        if int(paes[i])>maiorp:
            maiorp=int(paes[i])
        if int(paes[i])==menorp:
            contador2p=contador2p+1
    if contador2p==2:
        pontuacaop=pontuacaop+int(maiorp/2)
    for i in range(1,3):
        if int(willy[i])>maiorw:
            maiorw=int(willy[i])
        if int(willy[i])==maiorw:
            contador2w=contador2w+1
    if contador2w==2:
        pontuacaow=pontuacaow+int(maiorw/2)
    if (int(paes[0])+int(paes[1])+int(paes[2]))==8:
        pontuacaop=pontuacaop+8
    if (int(willy[0])+int(willy[1])+int(willy[2]))==8:
        pontuacaow=pontuacaow+8
    if pontuacaop>pontuacaow:
        vencedor=1
    elif pontuacaop<pontuacaow:
        vencedor=2
    return(vencedor)
paes=input().split()
paes=list(map(int,paes))
paes.sort()
willy=input().split()
willy.sort()
willy=list(map(int,willy))
print(pontuacao(paes,willy))