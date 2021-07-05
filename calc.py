try:
    valorCompra = float(input('Digite valor da compra: '))
    dinheiro = float(input('Digite valor fornecido pelo cliente: '))

except ValueError:
    print('\033[31m Use o Ponto no lugar da virgula para centavos ou digite um numero inteiro \033[0;0m')

else:
    valor = (dinheiro - valorCompra)

    print('Notas a serem entregue para troco de''\033[33m' + ' $' + '\033[0;0m' + '\033[32m {:.2f} \033[0;0m'.format(valor))
    print('\033[36m')

    print('--------NOTAS----------')

    while (valor > 1):

        if (valor >= 200):
            print("{} duzentos reais ".format(int(valor / 200)))
            valor = round(valor % 200, 2)
        elif (valor >= 100):
            print("{} Cem reais".format(int(valor / 100)))
            valor = round(valor % 100, 2)
        elif (valor >= 50):
            print("{} Cinquenta reais".format(int(valor / 50)))
            valor = round(valor % 50, 2)
        elif (valor >= 20):
            print("{} Vinte reais".format(int(valor / 20)))
            valor = round(valor % 20, 2)
        elif (valor >= 10):
            print("{} Dez reais".format(int(valor / 10)))
            valor = round(valor % 10, 2)
        elif (valor >= 5):
            print("{} Cinco reais".format(int(valor / 5)))
            valor = round(valor % 5, 2)
        elif (valor >= 2):
            print("{} Dois reais".format(int(valor / 2)))
            valor = round(valor % 2, 2)

    print('--------MOEDAS---------')

    while (valor <= 1):

        if (valor >= 1):
            print("{} Um real".format(int(valor / 1)))
            valor = round(valor % 1, 2)

        elif (valor >= 0.50):
            print("{} Cinquenta centavos".format(int(valor / 0.50)))
            valor = round(valor % 0.50, 2)

        elif (valor >= 0.25):
            print("{} Vinte e Cinco centavos ".format(int(valor / 0.25)))
            valor = round(valor % 0.25, 2)

        elif (valor >= 0.10):
            print("{} Dez centavos".format(int(valor / 0.10)))
            valor = round(valor % 0.10, 2)

        elif (valor >= 0.05):
            print("{} cinco centavos".format(int(valor / 0.05)))
            valor = round(valor % 0.05, 2)

        elif (valor >= 0.01):
            print("{} Um centavo".format(int(valor / 0.01)))
            valor = round(valor % 0.01, 2)

        else:
            break
