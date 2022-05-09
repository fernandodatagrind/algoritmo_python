# número par ou impar
#-----------------------

#entrada
numero = int(input('Informe um número: '))
#processamento
if numero % 2 == 0:
    if numero > 0:
        print(f'O número {numero} é par e possitivo.')
    else:
        print(f'O número {numero} é par e negativo.')
else:
    if numero > 0:
        print(f'O número {numero} é impar e possitivo.')
    else:
        print(f'O número {numero} é impar e negativo.')

             