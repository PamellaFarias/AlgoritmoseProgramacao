nnatural=int(input())
triangulo=0
inicio=1
if nnatural<3:
    print("Falso")
else:
    while triangulo<nnatural:
        triangulo=inicio*(inicio+1)*(inicio+2)
        if triangulo!=nnatural:
            inicio=inicio+1
    if triangulo==nnatural:
        print("%s * %d * %s = %s\nVerdadeiro" % (inicio,(inicio+1),(inicio+2),nnatural))
    else:
        print("Falso")