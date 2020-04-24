preco = float(input("preço do produto: "))
qtd = int(input("quantidade do produto: "))
pag = input("forma de pagamento: ")
tot = preco * qtd
if pag == 'dinheiro':
    tot = tot*0.75
else:
    tot = tot*1.10
print (tot)
