cha=int(input())
certas=0
respostas=input().split()
for j in range(5):
    if int(respostas[j]) == cha:
        certas=certas+1
print(certas)
