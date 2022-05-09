#estoque médio
#-----------------
#entrada
quantidade_minima = int(input('Informe a quantidade mínima de peças: '))
quantidade_maxima = int(input('informe a qauntidade máxima de peças: '))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saida
print(f'O estoque médio é {estoque_medio} peças.')