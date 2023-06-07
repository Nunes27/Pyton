"""
idade = int(input('Informe sua idade:'))

menor = 16
emancipado = 18
maior = 19

if idade <= menor:
    print('Você é menor de idade')
elif idade > menor and idade <= emancipado:
    print('Você é emancipado')
elif idade >= maior:
    print('Você é maior de idade')
"""
idade = int(input('Informe a idade: '))

infantil_a = 5
infantil_b = 8
juvenil_a = 11
juvenil_b = 14
end = 17

if idade >= infantil_a and idade < infantil_b:
    print('Categoria infantil A')
elif idade >= infantil_b and idade < juvenil_a:
    print('Categoria infantil B')
elif idade >= juvenil_a and idade < juvenil_b:
    print('Categoria juvenil A')
elif idade >= juvenil_b and idade <= end:
    print('Categoria Juvenil B')
