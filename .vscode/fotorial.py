'''
como achar o fatorial de um numero
'''
numero = int(input("Insira um numero: "))
fatorial = 1
if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0:
    print(f"O fatoria de {numero} é 1")
else:
    for x in range(1, numero+1):
        fatorial = fatorial*x

print(f'O fatoria de {numero} é: {fatorial}')
