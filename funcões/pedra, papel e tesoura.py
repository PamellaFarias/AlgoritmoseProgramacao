pm=0
pr=0
ganhador=""
for i in range(5):
    rita=input().lower()
    miguel=input().lower()
    while rita==miguel:
        rita=input().lower
        miguel=input().lower
    else:
        if miguel=="pedra":
            if rita=="tesoura":
                pm=pm+1
            elif rita=="papel":
                pr=pr+1
        if miguel=="tesoura":
            if rita=="papel":
                pm=pm+1
            elif rita=="pedra":
                pr=pr+1
        if miguel=="papel":
            if rita=="pedra":
                pm=pm+1
            elif rita=="tesoura":
                pr=pr+1
        
if pm>pr:
    ganhador="MIGUEL"
else:
    ganhador="MARIA"
print(pm,pr)