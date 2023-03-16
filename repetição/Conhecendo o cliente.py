vendas=0
valor_total=0.0
vtotal_cartao=0.0
idademenor=100
maiorcompra=0.0
vendas_vista=0
while True:
    idade=int(input())
    valor_compra=float(input())
    tipo_pagamento=input()
    continuar=input()
    vendas=vendas+1
    if tipo_pagamento=="V":
        valor_total=valor_total+valor_compra
        vendas_vista=vendas_vista+1
    else:
        vtotal_cartao=vtotal_cartao+valor_compra
    if idademenor>idade:
        idademenor=idade
    if maiorcompra<valor_compra:
        maiorcompra=valor_compra
    if continuar == "N":
        break
print(vendas)
if vendas_vista!=0:
    print("%.2f" %(valor_total))
else:
    print("0")
if vtotal_cartao>0:
    print("%.2f" %(vtotal_cartao))
else:
    print("0")
print(idademenor)       
print("%.2f" %(maiorcompra))
if vendas_vista!=0:
    print("%.2f" %(valor_total/vendas_vista))
else:
    print("0")
    
    
    
