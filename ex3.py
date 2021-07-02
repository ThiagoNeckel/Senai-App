valor = []
n = 0
soma = 0
while(n<20):
    entrada = int(input('digite valor Inteiro : '));
    valor.append(entrada);
    n += 1;

for total in valor:
    soma += total

media = soma/n

print(media);

if (media > 1) :
    print('Média é {} Positivo'.format(media))
else:
    print('Média é {} Negativa'.format(media))

