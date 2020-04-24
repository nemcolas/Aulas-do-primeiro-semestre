sb = float (input("Salário: "))
tempo = float(input("Tempo no banco: "))
emp = float(input("emprestimo: "))

if (sb >2000) :
    if (tempo>2):
        juros=emp*0.15
    else:
        juros=emp*0.2
    div=emp+juros
    print ('valor a ser pago',div)
else:
    print ("Empréstimo Negado")
