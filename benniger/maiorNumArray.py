"""
Descrição: Dado um array de números, encontre o maior valor.
Exemplo: [10, 5, 2, 8, 20] retorna 20.

"""
numeros = []
def maior_numero(numeros):
    numeroMaior = 0
    for numero in numeros:
        numeroAtual = numero
        if numeroAtual >= numeroMaior:
            numeroMaior = numeroAtual
    return numeroMaior


qtd_numeros = 0
while qtd_numeros < 3:
    numero_digitado = int(input(f'Digite um número: \n =>\t'))
    numeros.append(numero_digitado)
    qtd_numeros += 1

resultado = maior_numero(numeros=numeros)

print(f'O maior Número do Array é {resultado}')