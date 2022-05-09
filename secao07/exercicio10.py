#calssificar categoria
#-----------------------------

#entrada
idade = int(input('Informe sua idade: '))
#procesamento
if idade >= 5 and idade <= 7:
    print('infamtil A')
elif idade >= 8 and idade <= 11:
    print('infamtil B')
elif idade >= 12 and idade <= 13:
    print('juvenil A')
elif idade >= 14 and idade <= 17:
    print('juvenil B')
elif idade >= 18:
    print('adulto')