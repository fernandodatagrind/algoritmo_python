#"calcular salário"
#-------------------------------

#entrada
valor_por_hora = float(input('Informe valor pago por hora: '))
horas_trabalhadas = int(input('Informe horas trabalhadas no mês: '))
#processamento
salario = horas_trabalhadas * valor_por_hora
#saida
print(f'O valor do salário este mês é R${salario:0.2f}.')