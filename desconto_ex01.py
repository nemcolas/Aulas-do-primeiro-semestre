preco = float (input("diga o preço: "))
quant = int (input("diga a quantidade"))
valor = preco*quant
if ((valor >200) and (quant >5)) :
    valor=valor*0.9
print ("o valor é:" valor)
