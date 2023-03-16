def fmodelo(modelo):
    cmodelo=""    
    if modelo=="b" or modelo=="i" or modelo=="p":
        cmodelo=""
    else:
        cmodelo="Modelo de carro invalido"
    return(cmodelo)
def validatas(data,devolucao):
    diar=data[0]
    mesr=data[1]
    anor=data[2]
    diad=data[0]
    mesd=data[1]
    anod=data[2]
    if mesr == 4 or mesr == 6 or mesr == 9 or mesr==11:
        if diar>30:
            return("Data invalida")
    elif mesr==2:
        if diar>28:
            return("Data invalida")
    else:
        if diar>31:
            return("Data invalida")
        else:
            return("")
    if mesd == 4 or mesd == 6 or mesd == 9 or mesd==11:
        if diad>30:
            return("Data invalida")
        elif mesd==2:
            if diad>28:
                return("Data invalida")
        else:
            if diad>31:
                return("Data invalida")
            else:
                return("")
def datdev(data,devolucao):
    diar=data[0]
    mesr=data[1]
    anor=data[2]
    diad=data[0]
    mesd=data[1]
    anod=data[2]    

    if mesr>mesd:
        return("Data de devolucao inferior a data de locacao")
    elif anor>anod:
        return("Data de devolucao inferior a data de locacao")
    elif mesr==mesd:
        if diar>diad:
            return("Data de devolucao inferior a data de locacao")
        else:
            return()
    else:
        return()
def valodometro(odometro):
    if odometro[0]>odometro[1]:
        return("Valores do odometro com erro")
    else:
        return(odometro[1]-odometro[0])

def quantidadedias(data,devolucao):
    diar=data[0]
    mesr=data[1]
    anor=data[2]
    diad=data[0]
    mesd=data[1]
    anod=data[2]
    quantidadedias=0
    a1=0
    if mesr==mesd:
        if diar<diad:
            quantidadedias=diad-diar
    elif mesd-mesr==1: 
        if mesd == 4 or mesd == 6 or mesd == 9 or mesd==11:
            quantidadedias= 30-diad+diar        
        return(quantidadedias)

def valor_final(modelo,quantidadediasx,odometroc):
    valorlocacao=0
    if modelo=="b":
        valorlocacao=(30*quantidadediasx)+(0.30*odometroc)
    if modelo=="i":
        valorlocacao=(40*quantidadediasx)+(0.30*odometroc)
    if modelo=="p":
        valorlocacao=(60*quantidadediasx)+(0.30*odometroc)
    return(valorlocacao)

modelo=input()

modelos=[]
datas=[]
devolucoes=[]
odometros=[]

while modelo!="fim":
    
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
    
    quantidadequil=odometro[1]-odometro[0]
    validatasc=validatas(data,devolucao)
    datadevo=datdev(data,devolucao)
    modeloc=fmodelo(modelo)
    if valodometro(odometro)!="Valores do odometro com erro":
        odometroc=valodometro(odometro)
    quantidadediasx=quantidadedias(data,devolucao)
    if validatasc!="Data invalida" and datadevo!="Data de devolucao inferior a data de locacao" and modeloc!="Modelo de carro invalido" and odometroc!="Valores do odometro com erro":
        print(valor_final(modelo,quantidadediasx,odometroc))
    else:
        if modeloc=="Modelo de carro invalido":
            print(modeloc)
        if odometroc=="Valores do odometro com erro":
            print(odometroc)
        if validatasc=="Data invalida":
            print(validatasc)
        if datadevo=="Data de devolucao inferior a data de locacao":
            print(datadevo)

    modelo=input()



    