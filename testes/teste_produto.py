# teste_produto.py - confere a classe Produto

from produtos.produto import Produto

p = Produto("P001", "Luva de vaqueta", 12, 18.50)
print(p.listar_produtos())
p.entrada(5)
print(p.listar_produtos())
print(p.saida(4))
print(p.listar_produtos())
