public class LinkedList {
    public Node head;
    public Node tail;
    public int size;
    public java.util.Scanner scanner;

    // Construtor
    public LinkedList() {
        this.head = null;
        this.tail = null;
        this.size = 0;
        this.scanner = new java.util.Scanner(System.in);
    }

    public void printFirstThree() {
        Node current = head;
        for (int i = 0; i < 3; i++) {
            if (current != null) {
                System.out.print(current.value);
                if (current.next != null) {
                    System.out.print(" -> ");
                }
                current = current.next;
            }
        }
        System.out.println();

    }

    // PRINTS

    public void printList() {
        if (this.size > 200) {
            System.out.println("Lista muito grande para imprimir!");
            System.out.println("toma os 3 primeiros numeros:    ");
            printFirstThree();
        } else {

            // começa do começo k
            Node current = head;
            // enquanto o atual não for nulo
            while (current != null) {
                System.out.print(current.value);
                if (current.next != null) {
                    System.out.print(" -> ");
                }
                current = current.next;
            }
        }
        System.out.println();
    }

    public void printListIndex() {

        if (this.size > 200) {
            System.out.println("Lista muito grande para imprimir!");
            System.out.println("toma os 3 primeiros numeros:    ");
            printFirstThree();
        } else {

            Node current = head;
            int index = 0;
            while (current != null) {
                System.out.print("[" + index + ", " + current.value + "]");
                if (current.next != null) {
                    System.out.print(",  ");
                }
                current = current.next;
                index++;
            }
            ;
        }
        System.out.println();
    }

    // addlast
    public void addLast(int value) {
        // cria um novo item
        Node newNode = new Node(value);

        // se a lista está vazia então a cabeça e a cauda apontam para o novo item
        if (head == null) { // lista vazia
            head = newNode;
            tail = newNode;

            // se a lista não estiver vazia precisamos:
            // 1 dizer que o proximo da cauda atual é o novo item
            // 2 dizer que o anterior do novo item é a cauda atual
            // 3 atualizar a cauda para ser o novo item
        } else {
            tail.next = newNode;
            newNode.previous = tail;
            tail = newNode;
        }
        size++;
    }

    // addFirst
    public void addFirst(int value) {
        // cria um novo item
        Node newNode = new Node(value);

        // se a lista está vazia então a cabeça e a cauda apontam para o novo item
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head.previous = newNode;
            head = newNode;
        }
        size++;
    }

    // addAt
    public void addAt(int index, int value) {
        if (index < 0 || index > size) {
            throw new Error("Index inválido");
        }
        if (index == 0) {
            addFirst(value);
            return;
        }
        if (index == size) {
            addLast(value);
            return;
        }

        // cria o novo item
        Node newNode = new Node(value);

        // o atual é a cabeça, ou seja o começo da lista ligada,
        // percorre a lista até o index - 1 que queremos adicionar o novo item
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        // uma vez chegado no index que queremos temos que:

        // 1 dizer que o próximo do novo item é o próximo do atual
        newNode.next = current.next;

        // 2 dizer que o anterior do novo item é o atual
        newNode.previous = current;

        // 3 dizer que o próximo do atual é o novo item
        current.next.previous = newNode;

        // atualizar o próximo do atual para ser o novo item
        current.next = newNode;
        size++;
    }

    // agora metodos especificos para o atividade:

    public void verificaLista() {
        if (head == null) {
            throw new Error("Lista vazia");
        }
    }

    public void limparLista() {
        head = null;
        tail = null;
        size = 0;
    }

    public void removeFirst() {
        verificaLista();

        if (head == tail) {
            limparLista();

        } else {
            head = head.next;
            head.previous = null;
        }
        size--;
    }

    public void removeLast() {
        verificaLista();

        if (head == tail) {
            limparLista();
        } else {
            tail = tail.previous;
            tail.next = null;
        }
        size--;
    }

    public int removePrimeiroEncontrado(int value) {
        verificaLista();

        // verifica se o valor está na cabeça ou na cauda
        if (head.value == value) {
            removeFirst();
            return 0;
        }

        if (tail.value == value) {
            removeLast();
            return size + 1; // size original antes da remoção
        }

        // começa do começo
        Node current = head;
        int position = 0;
        // percorre a lista a partir do primeiro item
        while (current != null && current.value != value) {
            // enquanto o valor do item atual for diferente do valor que queremos remover ou
            // se chegarmos no final da lista
            current = current.next;
            position++;
        }

        // se chegarmos no final da lista e não encontramos o valor então perguntar ou
        // trohw error?

        if (current == null) {
            // throw new Error("Valor não encontrado");
            System.out.println("----------------------------------------------");
            System.out.println("Valor " + value + " não encontrado para remoção!");
            System.out.println();

            // java.util.Scanner scanner = new java.util.Scanner(System.in);

            // System.out.println("Deseja continuar a execução? (s/n): ");
            // String resposta = scanner.nextLine();
            // if (!resposta.equalsIgnoreCase("s")) {
            // System.out.println("Execução interrompida pelo usuário.");
            // scanner.close();
            // System.exit(0);
            // }
            return -1;
        }

        // se encontrarmos o valor então precisamos remover no meio ent trabalhar com
        // lógica, pega o
        current.previous.next = current.next; // o proximo do anterior do atual é o próximo do atual k
        if (current.next != null) {
            current.next.previous = current.previous; // se o próximo do atual não for nulo então o anterior do próximo
                                                      // do atual é o anterior do atual
        }
        size--;
        return position;
    }

    public int getValorPosicao(int index) {
        verificaLista();

        if (index < 0 || index >= size) {
            throw new Error("Index inválido");
        }

        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        return current.value;
    }

    public void matarLista() {

        System.out.println("Matando a lista...");
        head = null;
        tail = null;
        size = 0;
        scanner.close();
    }
}