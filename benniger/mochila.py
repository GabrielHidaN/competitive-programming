"""
Problema da Mochila: Dado um conjunto de itens, cada um com um peso e um valor, determine o número máximo de itens que podem ser colocados em uma mochila de capacidade limitada.
"""
import os

class Mochila:
    itens = list()
    capacidadeAtual = int(0)
    capacidadeTotal = int(300)

    def __init__(self, itensDisponiveis ,item):
        self.itensDisponiveis = itensDisponiveis
        self.item = item

    def adicionar(self):
            if (self.itensDisponiveis[self.item] + self.capacidadeAtual) <= self.capacidadeTotal:
                print('Adicionando Item...')
                print(f'Item:  {self.item}  Adicionado!')

                return self.item , self.itensDisponiveis[self.item] 
            else:
                print('Mochila Cheia')
                return None


    def listarItens(self):
        pass

    def remover(self):
        pass



while True:

    itensDisponiveis = {
    'kit': 50,
    'fruta': 50,
    'roupa': 100,
    'livro': 100,
    'arma': 100,
    'uva':310
    }

    menu = input('''

[1] Adicionar Item
[2] Remover Item
[3] Listar Item

 =>\t''')
    
    if menu == '1':
        os.system('clear')
        item = str(input('Digite o Item que Deseja Adicionar:\t'))
        try:
            if itensDisponiveis[item]:
                adicionarItem =  Mochila(item=item ,itensDisponiveis=itensDisponiveis)
                try:
                    novoItem , valorItem  = adicionarItem.adicionar()
                    Mochila.itens.append(novoItem)
                    Mochila.capacidadeAtual += valorItem
                except TypeError:
                    pass
        except KeyError:
            print('O produto não está registrado!')
        