faltas=10
mediamn=7
mediamx=9,5
def classifica(faltas,media):
    texto=""
    if faltas>10:
        texto="REPROVADO POR FALTAS"
    else:
        if media<7:
            texto="REPROVADO"
        else:
            if media>=9.5:
                texto="APROVADO COM LOUVOR"
            else:
                texto="APROVADO"  
    return(texto)
faltas=int(input())
media=float(input())
print(classifica(faltas,media))
    
    