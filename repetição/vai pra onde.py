cdd=""
d_km=0
p_valor=0.0
while True:
    cidade=input().upper()
    if cidade=="FIM":
        break
    distancia_km=int(input())
    passagem_valor=float(input())
    if ((distancia_km>d_km)and(passagem_valor>p_valor)and(passagem_valor*2<=300)):
        cdd=cidade
        d_km=distancia_km
        p_valor=passagem_valor
if cdd=="":
    print("SEM DESTINO")
else:
    print(cdd)
        
