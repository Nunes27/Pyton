"""

Exercicios - Python

observação: todos os exercicios devem utilizar a função input, de forma que o usuario possa determinar os dados de entrada
01 - area de um retangulo
02 - area de um retangulo
03 - se o produto que você quer avaliar custa (??) reais qual será o valor do mesmo com desconto de (??)%.
05 - area de um circulo
06 - conversão de reais para dolar
07 - conversão de dolar para reais

"""

"""print('Calcule a area de um retangulo')
base = input('Qual o tamanho da sua base; ')
altura = input('Qual a altura: ')

area = float(base) * float(altura)

print(f'Sua area é de {area}')"""

"""print('calculando um desconto')

valor = input('Insira o valor do produto: ')
desconto = input('Insira a porcentagem do desconto: ')
valor_final = float(valor) - (float(valor) * float(desconto)/100)

print(f'Seu valor com o desconto é de {valor_final}')"""

"""print('Calculando a area de um circulo')

pi = 3.141592
raio = input('Distancia do circulo: ')

area_circulo = float(pi) * (float(raio) ** 2)

print(f'A area do circulo é {area_circulo:.6f}')
"""

"""print('conversão de real para dolar')

dolar = input('Seu valor em dolar:')
real = 4.91
conversao_dolar_to_real = float(real) * float(dolar)
print(f'O valor de ${dolar} convertido para real fica R${conversao_dolar_to_real}')
"""

real = input('Seu valor em real:')
dolar = 0.20
coonversao_real_to_dolar = float(real) * float(dolar)
print(f'O valor de R${real} convertido para real fica ${coonversao_real_to_dolar}')
