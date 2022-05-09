#peso ideal
#----------------

#entrada
altura = float(input('Informe sua altura: '))
sexo = input('Informe seu sexo m/f: ')
#processamento
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print('Sexo não reconhecido')
#saida
print(f'Seu peso ideal é {peso_ideal:0.2f}')
