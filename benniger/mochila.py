"""
Problema da Mochila: Dado um conjunto de itens, cada um com um peso e um valor, determine o número máximo de itens que podem ser colocados em uma mochila de capacidade limitada.
"""
import os

class Mochila:
    itens = list()
    capacidadeAtual = int(0)
    capacidadeTotal = int(300)
    itensDisponiveis = {
    'kit': 50,
    'fruta': 50,
    'roupa': 100,
    'livro': 100,
    'arma': 100
    }

    def __init__(self, item):
        self.item = item

    def adicionar(self):
        try:
            if self.itensDisponiveis[self.item]:
                if (self.itensDisponiveis[self.item] + self.capacidadeAtual) <= self.capacidadeTotal:
                    print('Adicionando Item...')
                    print(f'Item:  {self.item}  Adicionado!')

                    return self.item , self.itensDisponiveis[self.item]
        except KeyError:
            print('Produto não está registrado!')
            return


    def listarItens(self):
        pass

    def remover(self):
        pass



while True:
    menu = input('''

[1] Adicionar Item
[2] Remover Item
[3] Listar Item

 =>\t''')
    
    if menu == '1':
        os.system('clear')
        item = str(input('Digite o Item que Deseja Adicionar:\t'))
        adicionarItem =  Mochila(item=item)
        novoItem , valorItem = adicionarItem.adicionar()

        Mochila.itens.append(novoItem)
        Mochila.capacidadeAtual += valorItem
