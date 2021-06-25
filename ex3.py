valor = []
n = 0
while(n<5):
    entrada = int(input('digite valor Inteiro : '));
    valor.append(entrada);
    n += 1;

media = sum(valor)/len(valor)

print(media);

if (media > 1) :
    print('Média é {} Positivo'.format(media))
else:
    print('Média é {} Negativa'.format(media))
