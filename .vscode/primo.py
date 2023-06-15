'''
Como descobrir numeros primos
'''

print(30 * "-")

numero = int(input('Insira um numero para descobrir se o mesmo é primo: '))

if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("esse não é primo")
            break
        else:
            print('Esse numero é primo')
else:
    print('Esse numero é igual ou menor que 1')

print(30 * "-")