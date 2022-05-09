#índice poluição
#---------------------------

#entrada
indice = float(input('Informe o índice de poluição: '))
#processamento
if indice >= 0.3 and indice < 0.4:
    print('Atenção Industrias do 1º Grupo devem suspender as atividades')
elif indice >= 0.4 and indice < 0.5:
    print('Atenção Industrias do 1º e 2º Grupo devem suspender as atividades')
elif indice >= 0.5:
    print('Atenção todos os Grupos devem suspender as atividades.')
