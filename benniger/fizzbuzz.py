"""
Escreva um programa que imprime os números de 1 a 100, mas para múltiplos de 3, imprima "Fizz" em vez do número, e para múltiplos de 5, imprima "Buzz". Para números múltiplos de ambos, imprima "FizzBuzz".

"""

def fizz_buzz(numero):
    for n in range(numero + 1):
        if ((n % 3) ==  0) and ((n % 5) ==  0) :
            print('FizzBuzz')
        elif ((n % 3) ==  0) :
            print('Fizz')
        elif((n % 5) ==  0):
            print('Buzz')
        else:
            print(n)

fizz_buzz(100)