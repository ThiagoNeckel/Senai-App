l = [5, 7, 2, 9, 4, 1, 3]

'''1.A'''
cont = 0
for item in l:

    if item != 0:
        cont = cont + 1

print('Tamanho da Lista:',cont)

'''1.B'''
maior = l[0]
for maiorNumero in l:
    if maiorNumero > maior:
        maior = maiorNumero

print('Maior valor: ',maior)

'''1.C'''
menor = l[0]

for menorNumero in l:
    if menorNumero < menor:
        menor = menorNumero

print('Menor valor: ',menor)

'''1.D'''
soma = 0

for total in l:
    soma += total

print('Soma: ',soma)

'''1.E'''
aux = 1

for x in range(0,cont):
    for y in range(0,cont):
        if l[x]<l[y]:
            aux = l[x]
            l[x] = l[y]
            l[y] = aux

print('Ordem Crescente: ',l)

'''1.F'''
for x in range(0,cont):
    for y in range(0,cont):
        if l[x]>l[y]:
            aux = l[x]
            l[x] = l[y]
            l[y] = aux
print('Ordem Decresente: ',l)