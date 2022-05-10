# Exercicios

## 1 - Indentifique os dados de entrada, processamento e saída no algoritmo abaixo: 

1. receber código da peça 
1. receber valor da peça
1. calcular o valor total da peça (quantidade * valor da peça)
1. mostrar o código da peça e seu valor total


### entrada:
1. receber o código da peça
1. receber i valor da peça

### processamento:
1. calcular o valor total da peça (quantidade * valor da peça)

### saída:
1. mostrar o código da peça e seu valor total


## 2 - Faça um algoritmo para "Calcular o estoque médio de um peça", sendo que:

estoque médio = (quatidade mínina + quantidade máxima) / 2

**estoque médio**

1. receber a quantidade mínina de peça
2. receber a quantidade máxima de peça
3. somar a quantidade mínina e quantidade máxima
4. dividir o resultado da soma por 2
5. mostrar o resultado da divisão

```python
#entrada
quantidade_minima = int(input('Informe a quantidade mínima de peças: '))
quantidade_maxima = int(input('informe a qauntidade máxima de peças: '))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saida
print(f'O estoque médio é {estoque_medio} peças.')
```

## 3 - Teste o algoritimo anterior com dados definidos por você.

| **quatidade minima** |**quantidade máxima**  |**estoque médio** |
|--|--|---|
| 50 |230  |150 |
| 30 | 130 | 80 |
| 380 | 30 | 205 |


### 4 - Faça um algoritmo que peça dois números e imprima a soma.

**"Soma dos números"**

1. receber o primeiro número
2. receber o segundo número
3. somar o primeiro com o segundo número
4. mostrar o resultado da soma

```python
#entrada
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
#processamento
soma = num1 + num2
#saida
print(f'O resultado da soma é {soma}')
```
### 5 - Faça um algoritmo que converte metros em centímetros.

formula : metros * 100 

**"converte metros em centimetros"**

1. receber o valor em metros
2. multiplicar os metros por 100 
3. mostrar o resultado da multiplição

```python
#entrada
metros = int(input('Informe o valor em metros: '))
#procesamento
centimetros = metros * 100
#saida
print(f'{metros} Metros em centímetros é {centimetros}.')
```

### 6 - Faça um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


**""calculo salário""**

1. receber a qauntidade de horas trabalhadas
2. recever o valor da hora 
3. multiplicar o número de horas trabalhadas pelo valor da hora
4. mostrar o resultado da multiplicação

```python
#entrada
valor_por_hora = float(input('Informe valor pago por hora: '))
horas_trabalhadas = int(input('Informe horas trabalhadas no mês: '))
#processamento
salario = horas_trabalhadas * valor_por_hora
#saida
print(f'O valor do salário este mês é R${salario:0.2f}.')
```

### 7 - tendo como dados de entrada a altura de uma pessoa, contrua um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:

(72.7 * altura) - 58

**""calcular o peso ideal""**

1. recebe o altura da pessoa 
2. multiplicar a altura por 72.7
3. subtrair resultado da multiplicação por 58
4. mostrar resultado da subtração

```python
#entrada
altura = float(input('Informe sua altura: '))
#procesamento
peso_ideal = (72.7 * altura) - 58
#saida
print(f'Seu peso ideal seria {peso_ideal:0.2f}.')
```
