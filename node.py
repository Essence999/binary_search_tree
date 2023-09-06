class Node:
    '''Classe representando o Nodo com o valor, filho esquerdo e filho direito.'''

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self._tree_str(self, 0, False)

    def _tree_str(self, node, depth, is_left):
        tree_str = ""
        if node.right is not None:
            tree_str += self._tree_str(node.right, depth + 1, False)
        tree_str += "    " * depth
        tree_str += ("└── " if is_left else "┌── ") + str(node.value) + "\n"
        if node.left is not None:
            tree_str += self._tree_str(node.left, depth + 1, True)
        return tree_str


def print_tree(node, indent="", prefix="Root: "):
    if node is not None:
        print(indent + prefix + str(node.value))
        indent += "│   "
        print_tree(node.left, indent, "├─L: ")
        print_tree(node.right, indent, "├─R: ")


def print_treev2(node, prefix="", is_left=True):
    if node is not None:
        print(prefix + ("├─ " if is_left else "└─ ") + str(node.value))
        child_prefix = prefix + ("│  " if is_left else "   ")
        print_treev2(node.left, child_prefix, True)
        print_treev2(node.right, child_prefix, False)
