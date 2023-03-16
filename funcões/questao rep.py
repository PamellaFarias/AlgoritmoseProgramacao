nm=[]
nm=input().split()
N=int(nm[0])
M=int(nm[0])

E1=[]
E2=[]
S=[]

for m in range(N):
    ls1,ls2=input().split()
    E1.append(ls1)
    E2.append(ls1)
for n in range(M):
    ss=input()
    S.append(ss)
    for m in range(len(S)):
        for n in range(N):
            if S[m] == E1[n]:
                S[m]=E2[n]
            elif texto[j] == letras_aux[k]:
              texto[j]=letras[k]



