import subprocess
import re
import json
import os
import numpy as np
import matplotlib.pyplot as plt



def extrair_metricas(output):
    """Extrai tempo e memória da saída"""
    # Regex que funciona para ambos os formatos, ignorando acentos
    time_match = re.search(r'Tempo de execu.+o: ([\d.]+) ms', output)
    memory_match = re.search(r'Memoria utilizada: ([\d.-]+) KB', output)

    if time_match and memory_match:
        return float(time_match.group(1)), float(memory_match.group(1))

    return None, None

def executar_comando(comando):
    """Executa comando e retorna tempo e memória"""
    try:
        result = subprocess.run(comando, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return extrair_metricas(result.stdout)
        else:
            print(f"    Erro: {result.stderr}")
    except Exception as e:
        print(f"    Exceção: {e}")
    return None, None

def salvar_dados(dados, arquivo="save.txt"):
    """Salva os arrays de resultados em um arquivo"""
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=2)
    print(f"Dados salvos em {arquivo}")

def carregar_dados(arquivo="save.txt"):
    """Carrega os arrays de resultados de um arquivo"""
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar {arquivo}.")
        return None

def criar_graficos_comparativos():
    

    # Calcular estatísticas
    algoritmos = ['Python Bubble', 'Python Quick', 'Go Bubble', 'Go Quick']
    dados_tempo = [python_bubble_tempos, python_quick_tempos, go_bubble_tempos, go_quick_tempos]
    dados_memoria = [python_bubble_memorias, python_quick_memorias, go_bubble_memorias, go_quick_memorias]

    medias_tempo = [np.mean(dados) for dados in dados_tempo]
    medias_memoria = [np.mean(dados) for dados in dados_memoria]

    # Criar subplot com 4 gráficos
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    cores = ['#FF6B6B', '#B64949', '#4CAF50', '#2E7D32']



    # 1. Barras - Tempo
    bars1 = ax1.bar(algoritmos, medias_tempo, color=cores)
    ax1.set_title('Tempo Médio de Execução')
    ax1.set_ylabel('Tempo (ms)')
    
    # Adicionar labels nas barras
    for bar, valor in zip(bars1, medias_tempo):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(medias_tempo)*0.01,
                f'{valor:.2f}', ha='center', va='bottom')




    # 2. Barras - Memória
    bars2 = ax2.bar(algoritmos, medias_memoria, color=cores)
    ax2.set_title('Memória Média Utilizada')
    ax2.set_ylabel('Memória (KB)')

    # Adicionar labels nas barras
    for bar, valor in zip(bars2, medias_memoria):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(medias_memoria)*0.01,
                f'{valor:.2f}', ha='center', va='bottom')


  


    # 3. Box Plot - Tempo
    # 3. Linha - Tempo por execução
    execucoes = range(1, 11)
    for i, (dados, alg) in enumerate(zip(dados_tempo, algoritmos)):
        ax3.plot(execucoes, dados, 'o-', label=alg, color=cores[i])
    ax3.set_xlabel('Execução')
    ax3.set_ylabel('Tempo (ms)')
    ax3.set_title('Tempo por Execução')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Scatter - Tempo vs Memória
    for i, alg in enumerate(algoritmos):
        ax4.scatter(medias_tempo[i], medias_memoria[i], c=cores[i], s=150, label=alg)
        # Adicionar labels nos pontos
        ax4.text(medias_tempo[i], medias_memoria[i] + max(medias_memoria)*0.01,
                f'{medias_tempo[i]:.2f}ms\n{medias_memoria[i]:.2f}KB', 
                ha='center', va='bottom', fontsize=9)
    ax4.set_xlabel('Tempo (ms)')
    ax4.set_ylabel('Memória (KB)')
    ax4.set_title('Tempo vs Memória')
    ax4.legend()

    plt.tight_layout()
    plt.savefig('save.png', dpi=300, bbox_inches='tight')
    plt.show()






# Arrays para armazenar resultados
python_bubble_tempos = []
python_bubble_memorias = []
python_quick_tempos = []
python_quick_memorias = []
go_bubble_tempos = []
go_bubble_memorias = []
go_quick_tempos = []
go_quick_memorias = []

print("=== EXECUTANDO TESTES MANUAIS ===\n")

# Perguntar se quer usar dados salvos
escolha = input("Deseja usar dados salvos? (s/n): ").strip().lower()

if escolha == 's' or escolha == 'sim':
    dados_salvos = carregar_dados()
    if dados_salvos:
        python_bubble_tempos = dados_salvos.get("python_bubble_tempos", [])
        python_bubble_memorias = dados_salvos.get("python_bubble_memorias", [])
        python_quick_tempos = dados_salvos.get("python_quick_tempos", [])
        python_quick_memorias = dados_salvos.get("python_quick_memorias", [])
        go_bubble_tempos = dados_salvos.get("go_bubble_tempos", [])
        go_bubble_memorias = dados_salvos.get("go_bubble_memorias", [])
        go_quick_tempos = dados_salvos.get("go_quick_tempos", [])
        go_quick_memorias = dados_salvos.get("go_quick_memorias", [])
        print("Dados carregados com sucesso!\n")
    else:
        print("Não foi possível carregar os dados. Executando testes...\n")
        escolha = 'n'
else:
    print("Executando testes...\n")

if escolha != 's' and escolha != 'sim':
    print("Cada algoritmo será executado 10 vezes.\n")

    # Executar Python Bubble Sort 10 vezes
    print("Python Bubble Sort:")
    for i in range(10):
        tempo, memoria = executar_comando("py python_bubble_sort.py")
        if tempo is not None:
            python_bubble_tempos.append(tempo)
            python_bubble_memorias.append(memoria)
            print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

    # Executar Python Quick Sort 10 vezes
    print("\nPython Quick Sort:")
    for i in range(10):
        tempo, memoria = executar_comando("py python_quick_sort.py")
        if tempo is not None:
            python_quick_tempos.append(tempo)
            python_quick_memorias.append(memoria)
            print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

    # Executar Go Bubble Sort 10 vezes
    print("\nGo Bubble Sort:")
    for i in range(3):
        tempo, memoria = executar_comando("go run go_bubble_sort.go")
        if tempo is not None:
            go_bubble_tempos.append(tempo)
            go_bubble_memorias.append(memoria)
            print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

    # Executar Go Quick Sort 10 vezes
    print("\nGo Quick Sort:")
    for i in range(10):
        tempo, memoria = executar_comando("go run go_quick_sort.go")
        if tempo is not None:
            go_quick_tempos.append(tempo)
            go_quick_memorias.append(memoria)
            print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

    # Salvar os dados após executar os testes
    dados_para_salvar = {
        "python_bubble_tempos": python_bubble_tempos,
        "python_bubble_memorias": python_bubble_memorias,
        "python_quick_tempos": python_quick_tempos,
        "python_quick_memorias": python_quick_memorias,
        "go_bubble_tempos": go_bubble_tempos,
        "go_bubble_memorias": go_bubble_memorias,
        "go_quick_tempos": go_quick_tempos,
        "go_quick_memorias": go_quick_memorias
    }
    salvar_dados(dados_para_salvar)
    print()

# Mostrar resultados dos arrays
print(f"\n=== ARRAYS DE RESULTADOS ===")
print(f"python_bubble_tempos = {python_bubble_tempos}")
print(f"python_bubble_memorias = {python_bubble_memorias}")
print()

print(f"python_quick_tempos = {python_quick_tempos}")
print(f"python_quick_memorias = {python_quick_memorias}")
print()

print(f"go_bubble_tempos = {go_bubble_tempos}")
print(f"go_bubble_memorias = {go_bubble_memorias}")
print()

print(f"go_quick_tempos = {go_quick_tempos}")
print(f"go_quick_memorias = {go_quick_memorias}")

# Calcular médias simples
print(f"\n=== MEDIAS ===")
if python_bubble_tempos:
    print(f"Python Bubble - Média: {sum(python_bubble_tempos)/len(python_bubble_tempos):.4f}ms")
if python_quick_tempos:
    print(f"Python Quick - Média: {sum(python_quick_tempos)/len(python_quick_tempos):.4f}ms")
if go_bubble_tempos:
    print(f"Go Bubble - Média: {sum(go_bubble_tempos)/len(go_bubble_tempos):.4f}ms")
if go_quick_tempos:
    print(f"Go Quick - Média: {sum(go_quick_tempos)/len(go_quick_tempos):.4f}ms")





# Análise gráfica 
criar_graficos_comparativos()
