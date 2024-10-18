def impa_ou_par(n):
  if n > 0:
    verificar = f'O número {n} é: par' if ((n % 2) == 0 ) else f'O número {n} é: impar'
    return verificar

  else:
    return 'Você deve enviar um Número positivo acima de 0 !'


numeroDigitado = int(input(f"digite o número que deseja verificar : \n => "))


print(impa_ou_par(numeroDigitado))
