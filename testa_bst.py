from aluno import Aluno
from bst import BinarySearchTree

print("Vamos criar uma BST com objetos da classe Integer:")

bst1 = BinarySearchTree()

print("Inserimos ", bst1.add(8))
print("Inserimos ", bst1.add(7))
print("Inserimos ", bst1.add(10))
print("Inserimos ", bst1.add(9))
print("Inserimos ", bst1.add(11))
print("Inserimos ", bst1.add(12))
print("Inserimos ", bst1.add(8))
print("Inserimos ", bst1.add(9))
print("Inserimos ", bst1.add(6))
print("Inserimos ", bst1.add(5))
print("Inserimos ", bst1.add(6))
print("Inserimos ", bst1.add(2))


print("Vamos mostrar a BST percorrendo em-ordem:")
bst1.em_ordem()
print("\nPré ordem:")
bst1.pre_ordem()
print("\nPós ordem:")
bst1.pos_ordem()
print("\nEm nível:")
bst1.em_nivel()

bst2 = BinarySearchTree()
print("Agora vamos criar uma BST (e percorrer pelos RGMs) de objetos da classe Aluno:")

bst2.add(Aluno("333", "Misaka Mikoto", "F", 9.7))
bst2.add(Aluno("555", "Misaki Shokuhou", "F", 7.9))
bst2.add(Aluno("111", "Accelerator", "M", 10))
bst2.add(Aluno("000", "Kamijou Touma", "M", 3.9))
bst2.add(Aluno("222", "Kakine Teitoku", "M", 9.8))
bst2.add(Aluno("444", "Mugino Shizuru", "F", 8.6))

print("Em ordem:")
bst2.em_ordem()
print("\nPós ordem:")
bst2.pos_ordem()
print("\nPré ordem:")
bst2.pre_ordem()
print("\nEm nível:")
bst2.em_nivel()
print("\nPré ordem iterativo:")
bst2.pre_ordem_iterativo()

print("\n")
print(bst2.get_menor_recursivo(bst2.root))
print(bst2.get_maior_iterativo())

print()
print(bst2.find(Aluno("444", "Mugino Shizuru", "F", 8.6)))
