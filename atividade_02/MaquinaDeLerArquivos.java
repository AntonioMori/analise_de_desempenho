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
            java.io.FileReader fileReader = new java.io.FileReader(caminho);
            java.io.BufferedReader bufferedReader = new java.io.BufferedReader(fileReader);

            // Ler primeira linha com os valores iniciais da lista
            String linha = bufferedReader.readLine();
            String[] valores = linha.split(" ");
            

            for (String valor : valores) {
                lista.addLast(Integer.parseInt(valor));
            }

            // Ler quantidade de ações
            linha = bufferedReader.readLine();
            qtdAcoes = Integer.parseInt(linha);

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
            for (int i = 0; i < qtdAcoes; i++) {
                linha = bufferedReader.readLine();
                executarAcao(linha);
            }
            //uma vez acabado tudo fechar o scanner
            
            
            lista.matarLista();
            // lista.scanner.close();
            bufferedReader.close();

            
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
                    int valorAntes = lista.getValorPosicao(posicao);
                    System.out.println();
                    System.out.println("Adicionou " + numero + " na posição " + posicao
                            + ", valor anterior dessa posição: " + valorAntes);
                    System.out.println();
                }
                lista.addAt(posicao, numero);

                break;
            case "R": // Remover
                int valorRemover = Integer.parseInt(partes[1]);
                int posicaoRemovido = lista.removePrimeiroEncontrado(valorRemover);

                if (debugMode) {
                    System.out.println();
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
        }
    }
}
