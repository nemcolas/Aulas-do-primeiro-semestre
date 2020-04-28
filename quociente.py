num = int (input('numerador: '))
den = int (input('denominador'))
q = 0
while num >= den:
    num -= den
    q += 1
print ('quociente: ', q)
