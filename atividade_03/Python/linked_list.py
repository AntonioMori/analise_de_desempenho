from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_first_three(self):
        current = self.head
        for i in range(3):
            if current is not None:
                print(current.value, end="")
                if current.next is not None:
                    print(" -> ", end="")
                current = current.next
        print()

    def print_list(self):
        if self.size > 200:
            print("Lista muito grande para imprimir!")
        else:
            current = self.head
            while current is not None:
                print(current.value, end="")
                if current.next is not None:
                    print(" ", end="")
                current = current.next
        print()

    def print_list_index(self):
        if self.size > 200:
            print("Lista muito grande para imprimir!")
        else:
            current = self.head
            index = 0
            while current is not None:
                print(f"[{index}, {current.value}]", end="")
                if current.next is not None:
                    print(",  ", end="")
                current = current.next
                index += 1
        print()

    def add_last(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.size += 1

    def add_first(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def add_at(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index inválido")

        if index == 0:
            self.add_first(value)
            return

        if index == self.size:
            self.add_last(value)
            return

        new_node = Node(value)
        current = self.head
        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        new_node.previous = current
        current.next.previous = new_node
        current.next = new_node
        self.size += 1

    def verifica_lista(self):
        if self.head is None:
            raise RuntimeError("Lista vazia")

    def limpar_lista(self):
        self.head = None
        self.tail = None
        self.size = 0

    def remove_first(self):
        self.verifica_lista()

        if self.head == self.tail:
            self.limpar_lista()
        else:
            self.head = self.head.next
            self.head.previous = None
        self.size -= 1

    def remove_last(self):
        self.verifica_lista()

        if self.head == self.tail:
            self.limpar_lista()
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.size -= 1

    def remove_primeiro_encontrado(self, value):
        self.verifica_lista()

        if self.head.value == value:
            self.remove_first()
            return 0

        if self.tail.value == value:
            self.remove_last()
            return self.size + 1

        current = self.head
        position = 0
        while current is not None and current.value != value:
            current = current.next
            position += 1

        if current is None:
            print("----------------------------------------------")
            print(f"Valor {value} não encontrado para remoção!")
            print()
            return -1

        current.previous.next = current.next
        if current.next is not None:
            current.next.previous = current.previous
        self.size -= 1
        return position

    def get_valor_posicao(self, index):
        self.verifica_lista()

        if index < 0 or index >= self.size:
            raise IndexError("Index inválido")

        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def matar_lista(self):
        print("Matando a lista...")
        self.head = None
        self.tail = None
        self.size = 0