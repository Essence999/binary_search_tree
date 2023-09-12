from aluno import Aluno
from bst import BST

print("Vamos criar uma BST com números inteiros:")

bst1 = BST()
numeros = [8, 7, 6, 9, 6, 5, 1, 2, 3, 4]
print(numeros)
for numero in numeros:
    bst1.add(numero)

bst1.atravessar_arvore()
print()

bst2 = BST()
print("Agora vamos criar uma BST (e percorrer pelos RGMs) de objetos da classe Aluno:")

bst2.add(Aluno("333", "Misaka Mikoto", "F", 9.7))
bst2.add(Aluno("555", "Misaki Shokuhou", "F", 7.9))
bst2.add(Aluno("111", "Accelerator", "M", 10))
bst2.add(Aluno("000", "Kamijou Touma", "M", 3.9))
bst2.add(Aluno("222", "Kakine Teitoku", "M", 9.8))
bst2.add(Aluno("444", "Mugino Shizuru", "F", 8.6))

bst2.atravessar_arvore()
