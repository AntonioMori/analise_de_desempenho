from maquina_de_ler_arquivos import MaquinaDeLerArquivos
import os

def main():
    maquina_topada = MaquinaDeLerArquivos()
    maquina_topada.debug_mode = False

    # Usar o separador de arquivo apropriado para o sistema operacional
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(script_dir, "arq-novo.txt")
    print(f"Lendo arquivo: {arquivo}")
    maquina_topada.ler_arquivo(arquivo)

if __name__ == "__main__":
    main()