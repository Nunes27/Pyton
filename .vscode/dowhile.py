"""
do while
COdigo para advinhar numero
"""
palpite = 1
numero = 9

while True:
    print('Advinhe qual o numero correto: ')
    palpite = int(input())
    if palpite == numero:
        print("Parabens! Você acertou")
        break
    else:
        print("Você errou.")
else:
    print('Erro na aplicação')
print(bool(palpite))

