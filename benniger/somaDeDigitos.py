'''1. Soma dos dígitos de um número
Descrição: Dado um número inteiro positivo, escreva um programa que some todos os seus dígitos.
Entrada: Um número inteiro positivo N.
Saída: A soma de seus dígitos.
Exemplo:
Entrada: 123
Saída: 6 (1 + 2 + 3)'''



def soma_digitos(N):
    soma = 0
    while N > 0:
        soma += N % 10 # Pega o último dígito
        N = N // 10     # Remove o último dígito
    return soma

# Entrada do número
N = int(input("Digite um número inteiro positivo: "))

# Saída: soma dos dígitos
resultado = soma_digitos(N)
print("A soma dos dígitos é:", resultado)
