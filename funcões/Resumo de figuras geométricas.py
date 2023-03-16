def quadrado(lados):
    if lados[0]<0:
        maiorq=-1
    else:
        maiorq=lados[0]**2
        areaq=0
    for i in range(1,len(lados)):
        if lados[i]<0:
            areaq=-1
        else:
            areaq=lados[i]**2
        if areaq>maiorq:
            maiorq=areaq
    return(maiorq)
def retangulo(bases,alturas):
    if bases[0]<0 or bases[0]<0:
        maiorr=-1
    else:
        maiorr=bases[0]*alturas[0]
        arear=0
    for i in range(1,len(bases)):
        if bases[i]<0 or alturas[i]<0:
            arear=-1
        else:
            arear=int(bases[i])*int(alturas[i])
        if arear>maiorr:
            maiorr=arear
    return(maiorr)
def circulo(raios):
    if raios[0]<0:
        maiorc=-1
    else:
        maiorc=3.14*int(raios[0])**2
        areac=0
    for i in range(1,len(raios)):
        if raios[i]<0:
            areac=-1
        else:    
            areac=3.14*raios[i]**2
        if areac>maiorc:
            maiorc=areac
    return(maiorc)
figura=input()
quantidade=0
quantidadec=0.0
lados=[]
bases=[]
alturas=[]
raios=[]
while figura!="sair":
    if figura=="q":
        lado=int(input())
        lados.append(int(lado))
        quantidade=quantidade+1
    if figura=="r":
        base=int(input())
        altura=int(input())
        bases.append(int(base))
        alturas.append(altura)
        quantidade=quantidade+1
    if figura=="c":
        raio=int(input())
        raios.append(raio)
        quantidade=quantidade+1
        quantidadec=quantidadec+1
    figura=input()
print("Maior circulo:","%.2f"%circulo(raios))
print("Maior retangulo:","%.2f"%(retangulo(bases,alturas)))
print("Maior quadrado:","%.2f"%quadrado(lados))
print("Quantidade de figuras",quantidade)
print("Percentual de circulos:","%.2f"%((quantidadec/quantidade)*100))