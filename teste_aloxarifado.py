
# teste_almoxarifado.py


from produto import Produto
from almoxarifado import Almoxarifado


# Cria o almoxarifado
almox = Almoxarifado("Lages")


# Adiciona os produtos
almox.adicionar(Produto("P001", "Luva de vaqueta", 12, 18.50))
almox.adicionar(Produto("P002", "Óculos de proteção", 3, 12.25))
almox.adicionar(Produto("P003", "Broca 8 mm", 0, 9.75))
almox.adicionar(Produto("P004", "Paquímetro 150 mm", 8, 85.00))


# Testa a busca
print("Busca P002:", almox.buscar("P002").nome)
print("Busca P999:", almox.buscar("P999"))


# Testa entrada e saída
print("Entrada P001:", almox.entrada("P001", 5))
print("Saída P004:", almox.saida("P004", 4))
print("Saída P003:", almox.saida("P003", 1))
print("Saída P999:", almox.saida("P999", 1))


# Mostra o estoque
print("=== Estoque ===")


for item in almox.listar():
    print(item["codigo"], "|", item["quantidade"], "|",
          item["preco"], "|", item["situacao"])


# Mostra os produtos que precisam de reposição
print("=== Solicitação de compra ===")


for item in almox.solicitacao_compra():
    print(item)


# Mostra o resumo
print("=== Resumo ===")


resumo = almox.para_dicionario()


print(resumo["unidade"], "|", resumo["total_produtos"], "produtos")
print("Valor em estoque: R$", almox.valor_estoque())