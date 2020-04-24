def aprovacao (nota, faltas):
    if nota > 7 and faltas < 5:
        print ('aprovado')
    else:
        print ('reprovado')
    return

n=float(input('nota: '))
f=int(input('faltas: '))
aprovacao(n, f)
