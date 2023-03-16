modelos=[]
datas=[]
devolucoes=[]
odometros=[]
rmodelos=[]
rdatas=[]
rdevolucoes=[]
rodometros=[]
rquantdias=[]
valoresfinais=[]
for i in range(len(modelos)):
    def fmodelo(modelos):
        cmodelo=""    
        if modelos[i]=="b" or modelos[i]=="i" or modelos[i]=="p":
            cmodelo=""
        else:
            cmodelo="Modelo de carro invalido"
        return(cmodelo)
    rmodelos.append(fmodelo(modelos))
    def validatas(datas,devolucoes):
        diar=datas[i][0]
        mesr=datas[i][1]
        anor=datas[i][2]
        diad=datas[i][0]
        mesd=datas[i][1]
        anod=datas[i][2]
        verificador=""
        
        if mesr == 4 or mesr == 6 or mesr == 9 or mesr==11:
            if diar>30:
                verificador="Data invalida"
        elif mesr==2:
            if diar>28:
                verificador="Data invalida"
        else:
            if diar>31:
                verificador="Data invalida"
        if mesd == 4 or mesd == 6 or mesd == 9 or mesd==11:
            if diad>30:
                verificador="Data invalida"
        elif mesd==2:
            if diad>28:
                verificador="Data invalida"
        else:
            if diad>31:
                verificador="Data invalida"
        return(verificador1)
    rdatas.append(validatas(datas,devolucoes))
    def verfloc(datas,devolucoes):
        diar=datas[i][0]
        mesr=datas[i][1]
        anor=datas[i][2]
        diad=datas[i][0]
        mesd=datas[i][1]
        anod=datas[i][2]
        verificador2=""
        if mesr>mesd:
            verificador2="Data de devolucao inferior a data de locacao"
        elif mesr==mesd:
            if diar>diad:
                verificador2="Data de devolucao inferior a data de locacao"
        return(verificador2)
    rdevolucoes.append(verfloc(datas,devolucoes))
    def valodometro(odometros):
        odomet=""
        if odometro[i][0]>odometro[i][1]:
            odomet="Valores do odometro com erro"
        return(odomet)
    rodometros.append(valodometro(odometros))

    def quantidadedias(datas,devolucoes):
        diar=datas[i][0]
        mesr=datas[i][1]
        anor=datas[i][2]
        diad=datas[i][0]
        mesd=datas[i][1]
        anod=datas[i][2]
        quantidadedias=0
        if mesr==mesd:
            if diad==diar:
                quantidadedias=1
            else:
                quantidadedias=diad-diar
        return(quantidadedias)
    rquantdias.append(quantidadedias(datas,devolucoes))

    def valor_final(rmodelos,rquantdias,rodometros):
        valorlocacao=0
        if rmodelos[i]=="b":
            valorlocacao=(30*quantidadedias)+(0.30*odometroc)
        if rmodelos[i]=="i":
            valorlocacao=(40*quantidadedias)+(0.30*odometroc)
        if rmodelos[i]=="p":
            valorlocacao=(60*quantidadedias)+(0.30*odometroc)
        return(valorlocacao)
    valoresfinais.append(valor_final(modelo,quantidadedias,odometroc))

modelo=input()
while modelo!="FIM":
    data=input().split("/")
    data=list(map(int,data))
    datas.append(data)
    devolucao=input().split("/")
    devolucao=list(map(int,devolucao))
    devolucoes.append(devolucao)
    odometro=input().split()
    odometro=list(map(int,odometro))
    odometros.append(odometro)
    modelos.append(modelo)
    modelo=input()

for i in range(modelos):
    if rdatas[i]!="Data invalida" and rdevolucoes[i]!="Data de devolucao inferior a data de locacao" and rmodelos[i]!="Modelo de carro invalido" and rodometros[i]="Valores do odometro com erro":
        print(valoresfinais[i])
    else:
        if rdatas[i]=="Data invalida"
            print(rdatas[i])
        if rdevolucoes[i]=="Data de devolucao inferior a data de locacao":
            print(rdevolucoes[i])
        if rmodelos[i]=="Modelo de carro invalido":
            print(rmodelos[i])
        if rodometros[i]=="Valores do odometro com erro":
            print(rodometros[i])


    