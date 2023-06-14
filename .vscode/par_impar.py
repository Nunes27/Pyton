"""
Como descobrir se um numero é impar ou par
"""
print(7 * '-')
numero = int(input('Insira um numero para saber se o mesmo é par: '))
if (numero % 2) == 0:
    print(f"{numero} é um numero par")
else:
    print(f'{numero} é um numero impar')
