homens=0
mulheres=0
salarios=0
soma=0.00
salhm=0.0
pmsalario=""
for i in range(10):
    salario=float(input())
    sexo=input()
    soma=soma+salario
    if sexo == "f":
        mulheres=mulheres+1
    else:
        homens=homens+1
        salhm=salhm+salario
    if salario>salarios:
        salarios=salario
        pmsalario=sexo
print(homens)
print(mulheres)
print("%.1f"%(soma/10))
print(pmsalario)
print("%.1f"%(salhm/homens))

    
            
    