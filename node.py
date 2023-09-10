class Node:
    '''Classe representando o Nodo com o valor, filho esquerdo e filho direito.'''

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self._tree_str(self, 0)

    def _tree_str(self, node, depth, is_left=None):
        tree_str = ""
        if node.right is not None:
            tree_str += self._tree_str(node.right, depth + 1, False)
        tree_str += "    " * depth
        if is_left is not None:
            tree_str += ("└── " if is_left else "┌── ")
        tree_str += str(node.value) + "\n"
        if node.left is not None:
            tree_str += self._tree_str(node.left, depth + 1, True)
        return tree_str
