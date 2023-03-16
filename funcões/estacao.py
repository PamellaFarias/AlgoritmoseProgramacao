def estacao(dia,mes):
    estacao=""
    if (dia>=21 and mes ==9) or (dia<=20 and mes ==12) or (mes==10) or (mes==11):
        estacao="PRIMAVERA"
    if (dia>=21 and mes ==12) or (dia<=20 and mes ==3) or (mes==1) or (mes==2):
        estacao="VERAO"
    if (dia>=21 and mes ==3) or (dia<=20 and mes ==6) or (mes==4) or (mes==5):
        estacao="OUTONO"
    if (dia>=21 and mes ==6) or (dia<=20 and mes ==9) or (mes==7) or (mes==8):
        estacao="INVERNO"
    return(estacao)
dia=int(input())
mes=int(input())
print(estacao(dia,mes))