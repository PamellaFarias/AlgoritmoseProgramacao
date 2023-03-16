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
        continue
    provaredacao=int(input())
    if provaredacao>100:
        print("Digite uma nota inferior a 100.")
        provaredacao=int(input())
    sexo=input()
    media=(provaobjetiva+provaredacao)/2
    candidatos=candidatos+1
    if media>= 60 and provaobjetiva>40 and provaredacao>40:
        aprovados=aprovados+1
        if sexo=="F":
            mulheres=aprovados
        elif sexo=="M":
            homens=homens+1
print(candidatos,"candidato(s) inscrito(s).")
print(aprovados,"candidato(s) aprovado(s).")
print(mulheres,"mulher(es) e",homens,"homem(ns)." )