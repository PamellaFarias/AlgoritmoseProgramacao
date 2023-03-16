numeros="0123456789"
def leet(palavra):
    quantidade=0
    novapalavra=""
    if palavra=="":
        novapalavra="erro"
        return(novapalavra,quantidade)
    for i in range(len(palavra)-1,-1,-1):
        if palavra[i] in numeros:
            novapalavra="numeros"
            quantidade=0
            return(novapalavra,quantidade)
        if novapalavra!="numeros":
            if palavra[i]=="a":
                novapalavra=novapalavra+"@"
                quantidade=quantidade+1
            elif palavra[i]=="e":
                novapalavra=novapalavra+"3"
                quantidade=quantidade+1
            elif palavra[i]=="i":
                novapalavra=novapalavra+"1"
                quantidade=quantidade+1
            elif palavra[i]=="o":
                novapalavra=novapalavra+"0"
                quantidade=quantidade+1
            elif palavra[i]=="t":
                novapalavra=novapalavra+"7"
                quantidade=quantidade+1
            elif palavra[i]=="s":
                novapalavra=novapalavra+"5"
                quantidade=quantidade+1
            else:
                novapalavra=novapalavra+palavra[i]
    return(novapalavra,quantidade)
palavra=input().lower()
a,b=leet(palavra)
print(a)
print(b)