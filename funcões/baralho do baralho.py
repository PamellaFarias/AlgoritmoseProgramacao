def crescente():
    if cartasp[0]+1==cartasp[1] and cartasp[1]+1==cartasp[2]:
        paes.append(cartasp[0])
    if cartasw[0]+1==cartasw[1] and cartasw[1]+1==cartasw[2]:
        willy.append(cartasp[0])
    iguais()
    print(paes,willy)
def iguais():
    if cartasp[0]==cartasp[1]==cartasp[2]:
        paes.append(cartasw[0])
    if cartasw[0]==cartasw[1]==cartasw[2]:
        willy.append(cartasw[0])
    menoresi()
def menoresi():
    if cartasp[0]==cartasp[1]:
        paes.append(cartasp[0]//2)
    if cartasw[0]==cartasw[1]:
        willy.append(cartasw[0]//2)
    maiores(i)
def maioresi():
    if cartasp[1]==cartasp[2]:
        paes.append(cartasp[2]//2)
    if cartasw[1]==cartasw[2]:
        willy.append(cartasw[2]//2)
    somaoito()
def somaoito():
    somapaes=0
    somawilly=0
    for i in range(len(cartasp)):
        somapaes=somapaes+cartasp[i]
    if somapaes ==8:
        paes.append(8)
    for i in range(len(cartasw)):
        somawilly=somawilly+cartasw[i]
    if somawilly ==8:
        willy.append(8)
paes=[]
willy=[]
cartasp=input().split()
casrtasp=list(map(int,cartasp))
cartasp.sort()
cartasw=input().split()
casrtasw=list(map(int,cartasw))
cartasw.sort()
n1=sum(paes)
n2=sum(willy)
print(paes,willy)
if n1==n2:
    print(0)
elif n1>n2:
    print(1)
else:
    print(2)
        
    
        