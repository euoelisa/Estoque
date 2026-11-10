

class Almoxarifado:
    # Cria o almoxarifado
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []


    # Adiciona um produto
    def adicionar(self, produto):
        self.produtos.append(produto)


    # Procura um produto pelo código
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None


    # Adiciona produtos no estoque
    def entrada(self, codigo, qtd):
        p = self.buscar(codigo)


        if p is None:
            return False


        p.entrada(qtd)
        return True


    # Retira produtos do estoque
    def saida(self, codigo, qtd):
        p = self.buscar(codigo)


        if p is None:
            return False


        return p.saida(qtd)


    # Lista os produtos
    def listar(self):
        lista = []


        for p in self.produtos:
            lista.append(p.listar_produtos())


        return lista


    # Separa os produtos que precisam ser repostos
    def solicitacao_compra(self):
        lista = []


        for p in self.produtos:
            if p.situacao() != "OK":
                lista.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": p.situacao()
                })


        return lista


    # Calcula o valor do estoque
    def valor_estoque(self):
        total = 0


        for p in self.produtos:
            total = total + (p.quantidade * p.preco)


        return total


    # Junta os dados do almoxarifado
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }