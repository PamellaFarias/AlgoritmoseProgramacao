modelo=["b","i","p"]
quantidadedias=[1,2,3]
odometroc=[1,2,3]
valoresfinais=[]
for i in range(len(modelo)):
    def valor_final(modelo,quantidadedias,odometroc):
        valorlocacao=0
        if modelo[i]=="b":
            valorlocacao=(30*quantidadedias[i])+(0.30*odometroc[i])
        if modelo[i]=="i":
            valorlocacao=(40*quantidadedias[i])+(0.30*odometroc[i])
        if modelo[i]=="p":
            valorlocacao=(60*quantidadedias[i])+(0.30*odometroc[i])
        return(valorlocacao)
    valoresfinais.append(valor_final(modelo,quantidadedias,odometroc))
print(valoresfinais)