qbandejas=int(input())
copos=0
conteudo=[]
for i in range (qbandejas):
    conteudo=input().split()
    if int(conteudo[0])>int(conteudo[1]):
        copos=copos+int(conteudo[1])
print(copos)