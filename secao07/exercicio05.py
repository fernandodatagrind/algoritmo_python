# calcular multa
#------------------

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

