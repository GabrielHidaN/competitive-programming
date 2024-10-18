'''
Descrição: Dada uma string, verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma maneira de trás para frente).
Entrada: Uma string.
Saída: Imprimir "Sim" se for um palíndromo, ou "Não" caso contrário.
Exemplo:
Entrada: "radar"
Saída: Sim
Entrada: "teste"
Saída: Não


'''
def verificar(P):
  palavraFormada = ''

  try:
    converter = int(P)
    flag = None

  except:
    flag = True

  if flag is True:
    contador = -1
    for letra in P:

      letra_atual = P[contador]
      palavraFormada = palavraFormada + letra_atual
      contador -=  1

    if palavraFormada == P:
      return 'Sim'
    else:
      return 'Não'
  else:
    return 'Você deve Enviar uma string!'

while True:
  verificação = verificar(input("digite a palavra que deseja verificar: \n =>\t"))
  print(verificação)
