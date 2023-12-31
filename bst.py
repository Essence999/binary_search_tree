from node import Node


class BST:
    def __init__(self):
        self.root = None
        # Atributo necessário para efetuar o balanceamento estático
        self.lista_aux = []

    def atravessar_arvore(self):
        print("\nVisualização da árvore pré-balanceamento:\n")
        print(self)
        print("\nEm ordem:")
        self.em_ordem()
        print("\nEm nível:")
        self.em_nivel()
        print("\nVisualização da árvore pós-balanceamento:\n")
        self.balancear()
        print(self)
        print("\nEm nível:")
        self.em_nivel()

    def __str__(self):
        return f"{self.root}"

    def is_empty(self):
        return self.root is None

    def add(self, valor):
        novo = Node(valor)
        self._add(novo, self.root)
        return valor

    def _add(self, novo, anterior=None):
        if self.root is None:
            self.root = novo
            return self.root
        if anterior is not None:
            if novo.value < anterior.value:
                anterior.left = self._add(novo, anterior.left)
            else:
                anterior.right = self._add(novo, anterior.right)
        else:
            anterior = novo
        return anterior

    def em_ordem(self):
        self._em_ordem(self.root)

    def _em_ordem(self, node):
        if node is not None:
            self._em_ordem(node.left)
            print(node.value)
            self._em_ordem(node.right)

    def pre_ordem(self):
        self._pre_ordem(self.root)

    def _pre_ordem(self, node):
        if node is not None:
            print(node.value)
            self._pre_ordem(node.left)
            self._pre_ordem(node.right)

    def pre_ordem_iterativo(self):
        if self.root is None:
            return
        pilha_aux = [self.root]
        while pilha_aux:
            node_aux = pilha_aux.pop()
            print(node_aux.value)
            if node_aux.right:
                pilha_aux.append(node_aux.right)
            if node_aux.left:
                pilha_aux.append(node_aux.left)

    def pos_ordem(self):
        self._pos_ordem(self.root)

    def _pos_ordem(self, node):
        if node is not None:
            self._pos_ordem(node.left)
            self._pos_ordem(node.right)
            print(node.value)

    def em_nivel(self):
        if self.root is None:
            return
        fila_aux = [self.root]
        while fila_aux:
            node_aux = fila_aux.pop(0)
            if node_aux.left:
                fila_aux.append(node_aux.left)
            if node_aux.right:
                fila_aux.append(node_aux.right)
            print(node_aux.value)

    # Determina o menor elemento a partir de um nó
    def get_menor_recursivo(self, node):
        if self.is_empty() or node is None:
            return None
        if node.left is None:
            return node.value
        else:
            return self.get_menor_recursivo(node.left)

    def get_menor_iterativo(self):
        if self.is_empty():
            return None

        no_aux = self.root
        while no_aux.left is not None:
            no_aux = no_aux.left

        return no_aux.value

    # Determina o maior elemento a partir de um nó
    def get_maior_recursivo(self, node):
        if self.is_empty():
            return None
        if node.right is None:
            return node.value
        return self.get_maior_recursivo(node.right)

    def get_maior_iterativo(self):
        if self.is_empty():
            return None

        no_aux = self.root
        while no_aux.right:
            no_aux = no_aux.right

        return no_aux.value

    # Retorna o nó com o maior valor da subárvore esquerda que começa em root.
    def get_max_left_node(self, root, parent):
        if self.is_empty():
            return None

        # Encontra o nó com o maior valor na subárvore esquerda
        while root.right:
            parent = root
            root = root.right

        # Agora, "root" contém o nó com o maior valor na subárvore esquerda
        if parent is not None:
            if parent.left == root:  # Se é filho esquerdo
                parent.left = root.left
            else:
                parent.right = root.left  # Atualize o pai da root
        return root.value

    def eliminar(self, element):
        return self._eliminar(self.root, None, element)

    # Remove um elemento da árvore, retorna true ou false
    def _eliminar(self, node, parent, element):
        if node is None:
            return False  # Elemento não encontrado
        if element == node.value:
            # Caso A: se node não possui filhos, basta eliminar o nó
            # Senão tiver pai, é a raiz da árvore.
            if parent is None:
                self.root = None
            # Senão o pai deve deserdar o filho
            elif node.left is None and node.right is None:
                self._substituir_nodo(node, parent, None)
            # Caso B1: se node só tiver o filho esquerdo
            elif node.right is None:
                self._substituir_nodo(node, parent, node.left)
            # Caso B2: se node só tiver o filho direito
            elif node.left is None:
                self._substituir_nodo(node, parent, node.right)
            # Caso C: o nodo node possui os dois filhos:
            else:
                node.value = self.get_max_left_node(node.left, node)
            # Fim dos casos em que o nó a eliminar foi encontrado, retornamos true
            return True
        # Se node não é o nó a eliminar, continuamos procurando.
        # Se o elemento for menor que o node, continuar procurando à esquerda:
        if element < node.value:
            return self._eliminar(node.left, node, element)
        # Senão, procurar à direita:
        return self._eliminar(node.right, node, element)

    def _substituir_nodo(self, node, parent, substitute):
        # Verifica se o nó que será eliminado é o filho esquerdo ou direito do pai:
        if parent.left == node:
            parent.left = substitute
        elif parent.right == node:
            parent.right = substitute
        else:
            self.root = substitute

    def search_bst(self, obj):
        return self._search_bst(self.root, obj)

    # Busca um elemento na árvore e retorna o nó onde encontrou,
    # ou null se não encontrou o nodo
    def _search_bst(self, node, obj):  # Procura obj a partir do nó node
        # Se a raiz for nula (árvore vazia) ou
        # chegou em uma folha => não achou o objeto procurado:
        if node is None:
            return None
        # Se achou o elemento, retornar o nó:
        if obj == node.value:
            return node
        # Se não achou, buscar recursivamente para a esquerda ou direita:
        if obj < node.value:
            return self._search_bst(node.left, obj)
        return self._search_bst(node.right, obj)

    # Algumas implementações de operações com BSTs em forma iterativa:
    def find(self, obj):
        if self.is_empty():
            return None

        current = self.root
        while current:  # Enquanto current não for None
            if obj == current.value:
                return current  # Retornamos o nodo encontrado
            if obj < current.value:
                current = current.left
            else:
                current = current.right
        return None  # Retornamos None se não encontramos o item procurado

    # Implementação iterativa da inserção na BST
    def insert(self, valor):
        try:
            novo_node = Node(valor)
        except MemoryError:
            return None  # Memória insuficiente

        if self.is_empty():
            self.root = novo_node  # Se a BST estiver vazia, inserimos na raiz
            return valor

        current = self.root  # Começamos procurando pela raiz
        while True:
            parent = current
            if valor < current.value:  # Verificamos se devemos ir para a esquerda
                current = current.left
                if current is None:  # Inserir à esquerda
                    parent.left = novo_node
                    break
            else:  # Ou ir para a direita
                current = current.right
                if current is None:  # Inserir a direita
                    parent.right = novo_node
                break
        return valor

    # Destruir a BST
    def destroy(self):
        self._destroy(self.root)

    def _destroy(self, node):
        if node is not None:
            self._destroy(node.left)
            self._destroy(node.right)
            self.eliminar(node.value)

    # IMPLEMENTAÇÕES PARA BALANCEAMENTO ESTÁTICO

    # Atravessamento em ordem para criar uma lista ordenada de menor a maior
    def carrega_lista(self, meio):
        if meio is not None:
            self.carrega_lista(meio.left)
            self.lista_aux.append(meio.value)
            self.carrega_lista(meio.right)

    def balanceamento_estatico(self, inicio, fim):
        if inicio <= fim:
            # Calcula a posição central do sub-vetor
            meio = (inicio + fim) // 2
            # Insere o valor na árvore
            self.add(self.lista_aux[meio])
            self.balanceamento_estatico(inicio, meio - 1)
            self.balanceamento_estatico(meio + 1, fim)

    def balancear(self):
        # Percorremos a BST em-ordem, para criar o vetor ordenado
        self.carrega_lista(self.root)
        # Destruímos a BST, que será criada novamente
        self.destroy()
        # Balanceamento estático: criamos a BST de novo
        self.balanceamento_estatico(0, len(self.lista_aux) - 1)
        # Limpamos o vetor para caso haver mais de um balanceamento
        self.lista_aux = []
