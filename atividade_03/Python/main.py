from maquina_de_ler_arquivos import MaquinaDeLerArquivos
import os

def main():
    maquina_topada = MaquinaDeLerArquivos()
    maquina_topada.debug_mode = False

    # Usar o separador de arquivo apropriado para o sistema operacional
    arquivo = os.path.join("arq-novo.txt")
    maquina_topada.ler_arquivo(arquivo)

if __name__ == "__main__":
    main()