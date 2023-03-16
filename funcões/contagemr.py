def contagem(n):
    contador=n
    for i in range(n,0,-1):
        for j in range(contador):
            if j==contador-1:
                print(i)
            else:
                print(i,end="-")
        contador=contador-1
n =int(input())
contagem(n)

        