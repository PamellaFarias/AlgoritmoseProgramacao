contresidencias=0
arrecadado=0.0
contexcedente=0
while True:
    quant_veiculos=int(input())
    if quant_veiculos==999:
        break
    if quant_veiculos>2:
        contresidencias=contresidencias+1
        contexcedente=contexcedente+quant_veiculos-2
        arrecadado=contexcedente*12.89
print("%.2f"% (arrecadado))
print(contresidencias)
        
    