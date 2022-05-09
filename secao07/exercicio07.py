#cáculo quadrado
#----------------------

#entrada
num1 = int(input('Informe o número 1: '))
num2 = int(input('Informe o número 2: '))
num3 = int(input('Informe o número 3: '))
num4 = int(input('Informe o número 4: '))
#processamento
q1 = num1 * num1
q2 = num2 * num2
q3 = num3 * num3
q4 = num4 * num4

if q3 >= 1000:
    print(q3)
else:
    print(f'Num1: {num1}, Quadrado: {q1}')
    print(f'Num2: {num2}, Quadrado: {q2}')
    print(f'Num3: {num3}, Quadrado: {q3}')
    print(f'Num4: {num4}, Quadrado: {q4}')
