x = int(input('Base: '))
n = int(input('Expoente: '))
pot = x
cont = 1

while (cont < n):
    x *= pot
    cont += 1
print(x)
