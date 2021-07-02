lista= ['ai',1,3,'oi',3.0,'10,00', True];

cont = 0
for item in lista:

    if item != 0:
        cont = cont + 1
        print(cont, item)