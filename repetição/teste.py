 n1=int(input())
 n2=int(input())
while True:
    if n1<1 or n1>9:
        print("Insira um número inicial entre 1 e 9")
    else:
        break
while True:
    if n2<1 or n2>9:
        print("Insira um número final entre 1 e 9")
    else:
        break
if n1>n2:
    print("Nenhuma tabuada nesse intervalo")
else:
    for j in range(n1,n2+1):
        for i in range (1,10):
            print("%s x %d = %s" % (j,i,(j*i)))
        print()
    
    