contador=0
n=int(input())
while n>0:
    for i in range(1,n+1):
        if n%i ==0:
            contador=contador+1
    if contador == 2:
        print("1")
    else:
        print("0",end)
    n=int(input())

