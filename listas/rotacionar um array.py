qint=int(input())
l=[]
for i in range(qint):
    n=int(input())
    l.append(n)   
deslocamentos=int(input())
for j in range(qint):
    if j+deslocamentos<qint:
        print(l[j+deslocamentos])
    else:
        print(l[(j+deslocamentos)-qint]) 