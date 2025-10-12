public class MaquinaDeLerArquivos {
    public LinkedList lista;
    public int qtdAcoes;
    public boolean debugMode;

    public MaquinaDeLerArquivos() {
        this.lista = new LinkedList();
        this.qtdAcoes = 0;
        this.debugMode = false;
    }

    public void lerArquivo(String caminho) {
        try {
            // Lê todo o arquivo de uma vez - mais eficiente
            byte[] bytes = java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(caminho));
            String content = new String(bytes, java.nio.charset.StandardCharsets.UTF_8);
            String[] linhas = content.split("\n");

            // Ler primeira linha com os valores iniciais da lista
            String[] valores = linhas[0].trim().split(" ");

            // Pre-size a lista para evitar realocações
            this.lista = new LinkedList(valores.length);

            // adiciona os valores na lista
            for (String valor : valores) {
                this.lista.addLast(Integer.parseInt(valor));
            }

            // Ler quantidade de ações
            qtdAcoes = Integer.parseInt(linhas[1].trim());

            if (debugMode) {

                System.out.println();
                System.out.println("----- DEBUG MODE LIGADO -----");
                System.out.println();

                System.out.println(" __    __     ______     ______     __   \r\n" + //
                        "/\\ \"-./  \\   /\\  __ \\   /\\  == \\   /\\ \\  \r\n" + //
                        "\\ \\ \\-./\\ \\  \\ \\ \\/\\ \\  \\ \\  __<   \\ \\ \\ \r\n" + //
                        " \\ \\_\\ \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\\r\n" + //
                        "  \\/_/  \\/_/   \\/_____/   \\/_/ /_/   \\/_/");

                System.out.println();
                System.out.println("Os prints com os índices só aparecerão no modo debug. O print das ações também.");
                System.out.println("[índice, valor]");

                System.out.println();
                System.out.println("Execução do código:");
                System.out.println();
            }

            // Executar as ações apenas da qtd de ações
            for (int i = 0; i < qtdAcoes && i + 2 < linhas.length; i++) {
                String linha = linhas[i + 2].trim();
                if (!linha.isEmpty()) {
                    executarAcao(linha);
                }
            }

        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
    }

    public void saveToFile(String caminho) {
        try {
            java.io.FileWriter fileWriter = new java.io.FileWriter(caminho);
            java.io.BufferedWriter bufferedWriter = new java.io.BufferedWriter(fileWriter);

            Node current = lista.head;
            while (current != null) {
                bufferedWriter.write(current.value + (current.next != null ? " " : ""));
                current = current.next;
            }
            bufferedWriter.newLine();
            bufferedWriter.close();
            System.out.println("Lista salva em " + caminho);
            System.out.println();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
    }

    private void executarAcao(String linha) {
        String[] partes = linha.split(" ");
        String acao = partes[0];

        switch (acao) {
            case "A": // Adicionar
                int numero = Integer.parseInt(partes[1]);
                int posicao = Integer.parseInt(partes[2]);

                if (debugMode) {
                    try {
                        int valorAntes = lista.getValorPosicao(posicao);
                        System.out.println("Adicionou " + numero + " na posição " + posicao
                                + ", valor anterior dessa posição: " + valorAntes);
                        System.out.println();
                    } catch (Exception e) {
                        System.out.println("Adicionou " + numero + " na posição " + posicao + " (posição estava vazia)");
                        System.out.println();
                    }
                }
                lista.addAt(posicao, numero);

                break;
            case "R": // Remover
                int valorRemover = Integer.parseInt(partes[1]);
                int posicaoRemovido = lista.removePrimeiroEncontrado(valorRemover);

                if (debugMode && posicaoRemovido != -1) {
                    System.out.println("Removeu " + valorRemover + " da posição " + posicaoRemovido);
                    System.out.println();
                }
                break;

            case "P": // Imprimir

                if (debugMode) {
                    lista.printListIndex();
                    // System.out.println();
                } else {
                    lista.printList();
                    System.out.println();

                }
                break;
            case "S": // SALVAR
                saveToFile("atividade_02\\output.txt");
                break;

        }
    }
}
