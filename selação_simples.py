preço = float (input('preço: '))
quantidade = int (input ('quantidade: '))
total = preço * quantidade
if total >150.00:
    print ('DESCONTO!')
    total = total * 0.9
else:
    print('SEM DESCONTO!')
print (total)


        
