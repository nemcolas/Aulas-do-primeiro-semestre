n = int(input('Digite um número para o calculo de Fatorial'))

cont=1
result=1

while cont <= n:
    result *=cont
    cont +=1
print ('o Fatorial desse numero é: ", result')
