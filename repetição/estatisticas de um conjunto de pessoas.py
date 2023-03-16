quant_mulheres=0
quant_homens=0
total_salarios=0.00
salario_mulheres=0.00
salario_homens=0.00
maior_salario_f=0.00
maior_salario_m=0.00
quant_salarios=0
d quant_salarios<11:
    salario = float(input())
    sexo=input()
    quant_salarios=quant_salarios+1
    total_salarios=total_salarios+salario
    if sexo=="f":
        quant_mulheres=quant_mulheres+1
        salario_mulheres=salario_mulheres+salario
        if maior_salario_f<salario_mulheres:
            maior_salario_f=salario
    else:
        quant_homens=quant_homens+1
        salario_homens=salario_homens+salario
        if maior_salario_m<salario_mulheres:
            maior_salario_m=salario
quant_salarios=0
salario = float(input())
print(quant_homens)
print(quant_mulheres)
if quant_salarios!=0 and total_salarios!=0:
    print("%.2f" %(total_salarios/quant_salarios))
if maior_salario_f>maior_salario_m:
    print("f")
else:
    print("m")
if salario_homens!=0 and quant_homens!=0:
    print("%.1f" %(salario_homens/quant_homens))    
    
    