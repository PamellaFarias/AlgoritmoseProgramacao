numero=1
n=int(input())
for M in range(1,n+1):
    numero=numero+1
    for R in range(1,numero):
        if R == numero-1:
            print(R,end="")
        else:
            print(R,end=" ")        
    print()

    