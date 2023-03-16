a = 0
b = 0
soma = 0
while True:
    n = int(input())
    if n == 999:
        break
    if n > 2:
        a += 1
        b += n-2
        soma = b * 12.89

    print(soma)
    print(a)