from produto import Produto

p1 = Produto()
p1.nome = "Esmalte Rísque"
p1.quantidade = 50
p1.preco = 7.99
p1.tipo = "esmalte"
p1.codigo = 124657

p2 = Produto()
p2.nome = "Fanta UVA"
p2.quantidade = 120
p2.preco = 10.00
p2.tipo = "refrigerante"
p2.codigo = 347821

p3 = Produto()
p3.nome = "Água Cristal"
p3.quantidade = 20
p3.preco = 2.99
p3.tipo = "agua"
p3.codigo = 229074

p4 = Produto()
p4.nome = "Fandangos"
p4.quantidade = 58
p4.preco = 12.00
p4.tipo = "salgadinho"
p4.codigo = 234158


print(p1.listar_produtos())
print(p2.listar_produtos())
print(p3.listar_produtos())
print(p4.listar_produtos())