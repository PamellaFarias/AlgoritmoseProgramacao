while True:
    n=int(input())
    fatorial=1
    if n<0:
        break
    for i in range(n,1,-1):
        fatorial=fatorial*i
    print(fatorial)

    