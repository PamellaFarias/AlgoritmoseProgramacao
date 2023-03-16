print("Insira os valores das doacoes:")
total_arrecadado=0.00
ndedoacoes=1
doacao=float(input())
if doacao<0:
    print("Total arrecadado: 0.00")
    print("Valor medio da doacao: 0.00")
else:
    while doacao>0:
        total_arrecadado=total_arrecadado+doacao
        ndedoacoes=ndedoacoes+1
        doacao=float(input())
    print("Total arrecadado: %.2f"%(total_arrecadado))
    print("Valor medio da doacao: %.2f"%(total_arrecadado/(ndedoacoes-1)))
    