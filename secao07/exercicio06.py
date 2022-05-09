#cálculo horas extras
#----------------------

#variaveis
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0
#entrada
c =int(input('Informe o código: '))
n = float(input('Informe a quantidade de horas trabalhadas: '))
#processamento
if n > 50:
    e = (n - 50) * valor_hora_excedente #20.00
    salario = (50 * valor_hora) + e #10.00
    print(f'Salário total R$ {salario:0.2f}')
    print(f'Salário excedente R$ {e:0.2f}')
else:
    salario = (n * valor_hora) #10.00
    print(f'Salário total R$ {salario:0.2f}')
    print(f'Salário excedente R$ {e:0.2f}')
