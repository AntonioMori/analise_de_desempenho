const fs = require('fs');
const path = require('path');
const LinkedList = require('./LinkedList.js');

class MaquinaDeLerArquivos {
    constructor() {
        this.lista = new LinkedList();
        this.qtdAcoes = 0;
        this.debugMode = false;
    }

    lerArquivo(caminho) {
        try {
            const data = fs.readFileSync(caminho, 'utf8');
            const linhas = data.split('\n').map(linha => linha.trim()).filter(linha => linha !== '');

            // Ler primeira linha com os valores iniciais da lista
            const valores = linhas[0].split(' ').map(Number);

            // Adiciona os valores na lista
            for (const valor of valores) {
                this.lista.addLast(valor);
            }

            // Ler quantidade de ações
            this.qtdAcoes = parseInt(linhas[1]);

            if (this.debugMode) {
                console.log();
                console.log("----- DEBUG MODE LIGADO -----");
                console.log();
                console.log(" __    __     ______     ______     __   ");
                console.log("/\\ \"-./  \\   /\\  __ \\   /\\  == \\   /\\ \\  ");
                console.log("\\ \\ \\-./\\ \\  \\ \\ \\/\\ \\  \\ \\  __<   \\ \\ \\ ");
                console.log(" \\ \\_\\ \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\");
                console.log("  \\/_/  \\/_/   \\/_____/   \\/_/ /_/   \\/_/");
                console.log();
                console.log("Os prints com os índices só aparecerão no modo debug. O print das ações também.");
                console.log("[índice, valor]");
                console.log();
                console.log("Execução do código:");
                console.log();
            }

            // Executar as ações apenas da qtd de ações
            for (let i = 0; i < this.qtdAcoes; i++) {
                if (i + 2 < linhas.length) {
                    const linha = linhas[i + 2];
                    if (linha) {
                        this.executarAcao(linha);
                    }
                }
            }

        } catch (error) {
            if (error.code === 'ENOENT') {
                console.log(`Arquivo ${caminho} não encontrado`);
            } else {
                console.log(`Erro ao ler arquivo: ${error.message}`);
            }
        }
    }

    saveToFile(caminho) {
        try {
            let current = this.lista.head;
            const valores = [];
            while (current !== null) {
                valores.push(current.value.toString());
                current = current.next;
            }
            fs.writeFileSync(caminho, valores.join(' ') + '\n');
            console.log(`Lista salva em ${caminho}`);
            console.log();
        } catch (error) {
            console.log(`Erro ao salvar arquivo: ${error.message}`);
        }
    }

    executarAcao(linha) {
        const partes = linha.trim().split(' ');
        const acao = partes[0];

        switch (acao) {
            case 'A': // Adicionar
                const numero = parseInt(partes[1]);
                const posicao = parseInt(partes[2]);

                if (this.debugMode) {
                    try {
                        const valorAntes = this.lista.getValorPosicao(posicao);
                        console.log(`Adicionou ${numero} na posição ${posicao}, valor anterior dessa posição: ${valorAntes}`);
                        console.log();
                    } catch {
                        console.log(`Adicionou ${numero} na posição ${posicao} (posição estava vazia)`);
                        console.log();
                    }
                }
                this.lista.addAt(posicao, numero);
                break;

            case 'R': // Remover
                const valorRemover = parseInt(partes[1]);
                const posicaoRemovido = this.lista.removePrimeiroEncontrado(valorRemover);

                if (this.debugMode) {
                    if (posicaoRemovido !== -1) {
                        console.log(`Removeu ${valorRemover} da posição ${posicaoRemovido}`);
                        console.log();
                    }
                }
                break;

            case 'P': // Imprimir
                if (this.debugMode) {
                    this.lista.printListIndex();
                } else {
                    this.lista.printList();
                }
                break;

            case 'S': // SALVAR
                this.saveToFile("output.txt");
                break;
        }
    }
}

module.exports = MaquinaDeLerArquivos;