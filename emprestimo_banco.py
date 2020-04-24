sb = float (input('salário bruto: '))
tempo = int (input ('tempo:'))
emp = float (input('valor de empréstimo: '))
if sb > 2000.00:
    if tempo > 2:
            juros = emp * 0.15
    else:
            juros = emp *0.20
    print: (emp + juros)
else:
    print ('empréstimo negado')
