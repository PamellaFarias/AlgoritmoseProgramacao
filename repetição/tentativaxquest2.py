candidatos=0
aprovados=0
mulheres=0
homens=0
while True:
    provaobjetiva=int(input())
    if provaobjetiva<0:
        break;
    if provaobjetiva>100:
        print("Digite uma nota inferior a 100.")
while True:
    provaredacao=int(input())
    if provaredacao>100:
        print("Digite uma nota inferior a 100.")
    sexo=input()
    media=(provaobjetiva+provaredacao)/2
    candidatos=candidatos+1
else:
    if media> 60 and provaobjetiva>40 and provaredacao>40:
        aprovados=aprovados+1
        if aprovados>0 and sexo=="F":
            mulheres=mulheres+1
        elif aprovados>0 and sexo=="M":
            homens=homens+1
print(candidatos," candidato(s) inscrito(s)"".")
print(aprovados," candidato(s) aprovado(s)"".")
print(mulheres," mulher(es) e",homens," homem(ns)""." )