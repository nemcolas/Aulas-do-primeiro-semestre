n1=int(input('digite o primeiro numero: '))
n2=int(input('digite o segundo numero: '))
n3=int(input('digite o terceiro numero: '))



if (n1>n2) and (n1>n3):
    print ('o maior numero foi: ',n1)
else:
    if(n2>n1) and (n2>n3):
        print('o maior numero foi: ',n2)
    else:
        print('o maior numero foi:', n3)
