from linked_list import LinkedList

class MaquinaDeLerArquivos:
    def __init__(self):
        self.lista = LinkedList()
        self.qtd_acoes = 0
        self.debug_mode = False

    def ler_arquivo(self, caminho):
        try:
            with open(caminho, 'r') as file:
                linhas = file.readlines()

            # Ler primeira linha com os valores iniciais da lista
            valores = list(map(int, linhas[0].strip().split()))

            # Adiciona os valores na lista
            for valor in valores:
                self.lista.add_last(valor)

            # Ler quantidade de ações
            self.qtd_acoes = int(linhas[1].strip())

            if self.debug_mode:
                print()
                print("----- DEBUG MODE LIGADO -----")
                print()
                print(" __    __     ______     ______     __   ")
                print("/\\ \"-./  \\   /\\  __ \\   /\\  == \\   /\\ \\  ")
                print("\\ \\ \\-./\\ \\  \\ \\ \\/\\ \\  \\ \\  __<   \\ \\ \\ ")
                print(" \\ \\_\\ \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\")
                print("  \\/_/  \\/_/   \\/_____/   \\/_/ /_/   \\/_/")
                print()
                print("Os prints com os índices só aparecerão no modo debug. O print das ações também.")
                print("[índice, valor]")
                print()
                print("Execução do código:")
                print()

            # Executar as ações apenas da qtd de ações
            for i in range(self.qtd_acoes):
                if i + 2 < len(linhas):
                    linha = linhas[i + 2].strip()
                    if linha:
                        self.executar_acao(linha)

        except FileNotFoundError:
            print(f"Arquivo {caminho} não encontrado")
        except Exception as e:
            print(f"Erro ao ler arquivo: {e}")

    def save_to_file(self, caminho):
        try:
            with open(caminho, 'w') as file:
                current = self.lista.head
                valores = []
                while current is not None:
                    valores.append(str(current.value))
                    current = current.next
                file.write(' '.join(valores) + '\n')
            print(f"Lista salva em {caminho}")
            print()
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")


    def executar_acao(self, linha):
        partes = linha.strip().split()
        acao = partes[0]

        if acao == "A":  # Adicionar
            numero = int(partes[1])
            posicao = int(partes[2])

            if self.debug_mode:
                try:
                    valor_antes = self.lista.get_valor_posicao(posicao)
                    print(f"Adicionou {numero} na posição {posicao}, valor anterior dessa posição: {valor_antes}")
                    print()
                except:
                    print(f"Adicionou {numero} na posição {posicao} (posição estava vazia)")
                    print()

            self.lista.add_at(posicao, numero)

        elif acao == "R":  # Remover
            valor_remover = int(partes[1])
            posicao_removido = self.lista.remove_primeiro_encontrado(valor_remover)

            if self.debug_mode:
                if posicao_removido != -1:
                    print(f"Removeu {valor_remover} da posição {posicao_removido}")
                    print()

        elif acao == "P":  # Imprimir
            if self.debug_mode:
                self.lista.print_list_index()
            else:
                self.lista.print_list()

        elif acao == "S":  # SALVAR
            self.save_to_file("output.txt")

