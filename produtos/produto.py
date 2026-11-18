# produto.py - classe Produto

class Produto:
    # Cria um produto com seus dados
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    # Informa a situação do estoque
    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 4:
            return "Repor"
        else:
            return "OK"

    # Devolve os dados do produto
    def listar_produtos(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "situacao": self.situacao()
        }

    # Soma a quantidade que chegou
    def entrada(self, qtd):
        self.quantidade = self.quantidade + qtd

    # Retira a quantidade se tiver estoque
    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = self.quantidade - qtd
            return True
        return False
