string=input()
i=0
j=0
cont=0
proxima=""
while i<len(string):
    if(i!=0) or string[0]!=" ":
        proxima=proxima+string[i]
    if string[i]==" ":
        j=i+1
        while string[j]==" ":
            j=j+1
            i=j-1
        if string[j] !=" ":
            cont=cont+1
    i=i+1
print(cont+1)
    
    