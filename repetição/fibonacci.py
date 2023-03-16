while True:
    v1=0
    v2=1
    v3=0
    n=int(input())
    if n==0:
        break
    if n ==1:
        print("0")
    elif n==2:
        print("0 1")
    else:
        print("0 1",end=" ")
        for i in range(0,n-2):
            v3=v1+v2
            v1=v2
            v2=v3
            if i<n-3:
                print(v3,end=" ")
            else:
                print(v3)
            
            
        
        
    