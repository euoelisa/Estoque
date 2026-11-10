from produtos.produto import Produto

p1 = Produto(124657, "Esmalte Rísque", 50, 7.99)
p1.tipo = "esmalte"

p2 = Produto(347821, "Fanta UVA", 120, 10.00)
p2.tipo = "refrigerante"

p3 = Produto(229074, "Água Cristal", 20, 2.99)
p3.tipo = "agua"

p4 = Produto(234158, "Fandangos", 58, 12.00)
p4.tipo = "salgadinho"


print(p1.listar_produtos())
print(p2.listar_produtos())
print(p3.listar_produtos())
print(p4.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos())

p1.saida(15)
print(p1.listar_produtos())
