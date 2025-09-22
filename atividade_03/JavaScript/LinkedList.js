const Node = require('./Node.js');

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    printFirstThree() {
        let current = this.head;
        for (let i = 0; i < 3; i++) {
            if (current !== null) {
                process.stdout.write(current.value.toString());
                if (current.next !== null) {
                    process.stdout.write(" -> ");
                }
                current = current.next;
            }
        }
        console.log();
    }

    printList() {
        if (this.size > 200) {
            console.log("Lista muito grande para imprimir!");
        } else {
            let current = this.head;
            let output = [];
            while (current !== null) {
                output.push(current.value);
                current = current.next;
            }
            console.log(output.join(" "));
        }
    }

    printListIndex() {
        if (this.size > 200) {
            console.log("Lista muito grande para imprimir!");
        } else {
            let current = this.head;
            let index = 0;
            let output = [];
            while (current !== null) {
                output.push(`[${index}, ${current.value}]`);
                current = current.next;
                index++;
            }
            console.log(output.join(",  "));
        }
    }

    addLast(value) {
        const newNode = new Node(value);

        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.previous = this.tail;
            this.tail = newNode;
        }
        this.size++;
    }

    addFirst(value) {
        const newNode = new Node(value);

        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head.previous = newNode;
            this.head = newNode;
        }
        this.size++;
    }

    addAt(index, value) {
        if (index < 0 || index > this.size) {
            console.log("----------------------------------------------");
            console.log(`Índice ${index} inválido para adição! Tamanho atual da lista: ${this.size}`);
            console.log();
            return;
        }

        if (index === 0) {
            this.addFirst(value);
            return;
        }

        if (index === this.size) {
            this.addLast(value);
            return;
        }

        const newNode = new Node(value);
        let current = this.head;
        for (let i = 0; i < index - 1; i++) {
            current = current.next;
        }

        newNode.next = current.next;
        newNode.previous = current;
        current.next.previous = newNode;
        current.next = newNode;
        this.size++;
    }

    verificaLista() {
        if (this.head === null) {
            throw new Error("Lista vazia");
        }
    }

    limparLista() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    removeFirst() {
        this.verificaLista();

        if (this.head === this.tail) {
            this.limparLista();
        } else {
            this.head = this.head.next;
            this.head.previous = null;
        }
        this.size--;
    }

    removeLast() {
        this.verificaLista();

        if (this.head === this.tail) {
            this.limparLista();
        } else {
            this.tail = this.tail.previous;
            this.tail.next = null;
        }
        this.size--;
    }

    removePrimeiroEncontrado(value) {
        this.verificaLista();

        if (this.head.value === value) {
            this.removeFirst();
            return 0;
        }

        if (this.tail.value === value) {
            this.removeLast();
            return this.size + 1;
        }

        let current = this.head;
        let position = 0;
        while (current !== null && current.value !== value) {
            current = current.next;
            position++;
        }

        if (current === null) {
            console.log("----------------------------------------------");
            console.log(`Valor ${value} não encontrado para remoção!`);
            console.log();
            return -1;
        }

        current.previous.next = current.next;
        if (current.next !== null) {
            current.next.previous = current.previous;
        }
        this.size--;
        return position;
    }

    getValorPosicao(index) {
        this.verificaLista();

        if (index < 0 || index >= this.size) {
            throw new Error("Index inválido");
        }

        let current = this.head;
        for (let i = 0; i < index; i++) {
            current = current.next;
        }
        return current.value;
    }

    matarLista() {
        console.log("Matando a lista...");
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
}

module.exports = LinkedList;