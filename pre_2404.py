def fatorial () :
    n = int (input('Digite um número para calcular o fatorial: '))

    r=1
    c=1

    while c<=n:
        r*=c
        c+=1
    print ('O Fatorial desse número é', r)

while True:
    fatorial ()



