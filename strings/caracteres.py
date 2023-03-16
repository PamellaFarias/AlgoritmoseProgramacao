t=int(input())
while t!=0:
    s=input()
    inverso=''
    for i in range (t,0,-1):
        inverso=inverso+s[i-1]
    t=int(input())
    print (inverso)
