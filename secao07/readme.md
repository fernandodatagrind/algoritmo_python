## Exercicio 1  
Ler uma variável numérica n e imprimi-la somente se a mesma for maior que 100, caso contrário imprimila com o valor zero.

- receber valor  
se valor < 100 entao  
 escrever valor  
- senao   
	valor = 0  
	escrever valor

```python
#entrada
n = int(input('Informe um número: '))
#processamento
if n > 100:
    print(n)
else:
    print(0)
```

## Exercicio 2  

Elabore um algoritmo que leia um número. Se positivo armazene-o em "a"
se for negativo, em "b". No final mostrar o resultado.  

- receber valor
se valor > 0  entao  
	* a =  valor  
	escrever "valor positivo"  
	escrever a   
- senao   
	* b = valor  
	escrever "valor negativo"  
- escrever b

```python
#entrada
numero = int(input('Informe um número: '))
#processamento
if numero > 0:
    a = numero
    print('valor possitivo')
else:
    b = numero
    print('valor negativo')
print(numero)
```

## Exercicio 3  

Ler um número e verificar se ele é par ou ímpar. Quando for par armazenar 
esse valor em "p" e quando for ímpar armazená-lo em "i".
Exibir "p" e "i" no final do processamento.  

- p = 0
- i = 0   
- receber valor   
- se (valor % 2 == 0)  
	* p = valor
- senao
	* i = valor  
escrever p   
escrever i

```python
#variaveis
p = 0
i = 0
#entrada
numero = int(input('Informe um número: '))
#processamento
if numero % 2 == 0:
    p = numero
else:
    i = numero
print(p)
print(i)
```

# Exercicio 4  

Tendo como dados de entrada a altura e o sexo de uma pessoa, cosntrua
um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7 * altura) - 58
Para mulheres: (62.1 * altura) - 44.7  
 
- receber  altura 
- receber sexo
- se sexo == 'm' 
	* peso_ideal = (72.7 * altura) - 58
- se sexo == 'f'
	* peso_ideal = (62.1 * altura) - 44.7
- escrever peso_ideal

```python
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
```

## Exercicio 5 

João da Silva, pescador, comprou um microcomputador para controlar o 
rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4.00 por quilo excedente.  
João precisa que você faça um algoritmo que leia a variável 'p' (peso de peixes)
e verifique se há excesso. Se houver, garavar na variável 'e' (excesso)
e na variável 'm' o valor da multa que João deverá pagar. Caso contrário mostrar
tais variáveis com o conteúdo 'zero'.  

- e = 0
- m = 0
- receber peso "p"
- se p > 50 entao
	* calcular e = p - 50
	* calcular m = e * 4
	
- escrever "Peso: " + p
- escrever " Excesso: " + e
- escrever "Multa:" + m  

```python
#entrada
p = int(input('Informe o peso dos peixes: '))
#processamento
if p > 50:
    m = (p - 50) * 4.00
    e = 'excesso'
    print(f'Você devera pagar R$ {m:0.2f}')
else:
    e = 0
    m = 0
print(f'Peso: {p}')
print(f'Excesso: {e}')
print(f'Multa: {m}')
```

## Exercicio 6 	

Elabore um algoritmo que leia as variáveis 'c' e 'n', respectivamente código 
e número de horas trabalhadas de um operário. Calcule o salário sabendo-se que
ele ganha 10.00 por hora.   
Quando o número de horas exceder a 50 calcule o
excesso de pagamento armazenado-o na variável 'e'. Caso contrário zerar tal variável.
A hora excedente de trabalho vale 20.00. No final do processamento imprimeir o 
salário total e o salário excedente. 

- e = 0
- receber c 
- receber n 
- se n > 50 entao
	* calcular e =  n - 50
	* calcular n = n - e 
- extra = e * 20
- salario = n * 10
- escrever "Salário" +  salario
- escrever "Extra + extra

```python
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
```

## Exercicio 7


Desenvolva um algoritmo que :  
a) Leia 4 (quatro) números;  
b) Calcule o quadrado de cada um;  
c) Se o valor resultante do quadrado do terceiro for >= 100, imprima-o e finalize;  
d) Caso constrario, imprima os valores lidos e seus respectivos quadrados.  

- receber n1 
- receber n2  
- receber n3  
- receber n4 

- calcular q1 = n1  **  2
- calcular q2 = n2  **  2
- calcular q3 = n3  **  2
- calcular q4 = n4  **  2
- se resultado de q3 >= 100 entao
	* escrever resultado de q3
- senao
	
	* escrever resultado de n1, n2, n3, n4
	
```python
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
```

## Exercicio 8

Faça um algoritmo que leia um número inteiro e mostre uma mensagem 
indicando se este número e par ou impar, e se é possitivo ou negativo.


- receber n1
- se (n1 % 2 == 0) entao
	* escrever "numero par"
- senao
	* escrever "numero impar"
  
```python
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
```

## Exercicio  9

A Secretaria de Meio Ambiente que controla o índice de poluição mantén 3
grupos de indústrias que são altamente poluentes do meio ambiente. O índice de 
poluição aceitável varia de 0.5 ate 0.25. Se o índice sobe para 0.3 as indústrias 
do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0.4
as indúsrias do 1º grupo e 2º grupo são intimadas a sespender suas atividades, se o índice 
atingir 0.5 todos os grupos devem ser notificados a paralisarem suas atividades.  
Faça um algoritmo que leia o índice de poluição medido e emita a notifição adequada aos diferentes 
grupos de empresas. 

- receber indice 

- se (indice >= 0.3) e (poluicao < 0.4) entao 
	* escrever " notificar e supender atividades 1º grupo"
- se (indice >= 0,4) e (indice < 0.5) entao
	* escrever "notificar e supender atividades 2º e 3º grupos"
- se indice > 0,5) entao
	* escrever "todos os grupos suspender  atividade"
- senao
	* escrever "Niveis aceitáveis"

```python
#entrada
indice = float(input('Informe o índice de poluição: '))
#processamento
if indice >= 0.3 and indice < 0.4:
    print('Atenção Industrias do 1º Grupo devem suspender as atividades')
elif indice >= 0.4 and indice < 0.5:
    print('Atenção Industrias do 1º e 2º Grupo devem suspender as atividades')
elif indice >= 0.5:
    print('Atenção todos os Grupos devem suspender as atividades.')
```

## Exercicio 10

Elabore um algoritmo que dada idade de um nadador classifique-o em
uma das seguintes categorias:  
infantil-a = 5 a 7 anos  
infantil-b = 8 a 11 anos  
juvenil-a = 12 a 13 anos  
juvenil-b = 14 a 17 anos  
adultos = maiores de 18 anos  
  

- receber idade
- se idade >= 5 e idade <= 7 entao
	* escrever "infantil-a"
- se idade >= 8 e idade <= 11 entao
	* escrever "infantil-b"
- se idade >= 12 e idade <= 13 entao
	* escrever "juvenil-a"
- se idade >= 14 e idade <= 17 entao
	* escrever "juvenil=b"
- se idade >= 18 entao
	* escrever "adultos"

```python
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
```
