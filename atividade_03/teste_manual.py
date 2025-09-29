import subprocess
import re

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

# Arrays para armazenar resultados
python_bubble_tempos = []
python_bubble_memorias = []
python_quick_tempos = []
python_quick_memorias = []
js_bubble_tempos = []
js_bubble_memorias = []
js_quick_tempos = []
js_quick_memorias = []

print("=== EXECUTANDO TESTES MANUAIS ===\n")

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

# Executar JavaScript Bubble Sort 10 vezes
print("\nJavaScript Bubble Sort:")
for i in range(10):
    tempo, memoria = executar_comando("node javascript_bubble_sort.js")
    if tempo is not None:
        js_bubble_tempos.append(tempo)
        js_bubble_memorias.append(memoria)
        print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

# Executar JavaScript Quick Sort 10 vezes
print("\nJavaScript Quick Sort:")
for i in range(10):
    tempo, memoria = executar_comando("node javascript_quick_sort.js")
    if tempo is not None:
        js_quick_tempos.append(tempo)
        js_quick_memorias.append(memoria)
        print(f"  {i+1}: {tempo:.4f}ms, {memoria:.4f}KB")

# Mostrar resultados dos arrays
print(f"\n=== ARRAYS DE RESULTADOS ===")
print(f"python_bubble_tempos = {python_bubble_tempos}")
print(f"python_bubble_memorias = {python_bubble_memorias}")
print(f"python_quick_tempos = {python_quick_tempos}")
print(f"python_quick_memorias = {python_quick_memorias}")
print(f"js_bubble_tempos = {js_bubble_tempos}")
print(f"js_bubble_memorias = {js_bubble_memorias}")
print(f"js_quick_tempos = {js_quick_tempos}")
print(f"js_quick_memorias = {js_quick_memorias}")

# Calcular médias simples
print(f"\n=== MEDIAS ===")
if python_bubble_tempos:
    print(f"Python Bubble - Média: {sum(python_bubble_tempos)/len(python_bubble_tempos):.4f}ms")
if python_quick_tempos:
    print(f"Python Quick - Média: {sum(python_quick_tempos)/len(python_quick_tempos):.4f}ms")
if js_bubble_tempos:
    print(f"JS Bubble - Média: {sum(js_bubble_tempos)/len(js_bubble_tempos):.4f}ms")
if js_quick_tempos:
    print(f"JS Quick - Média: {sum(js_quick_tempos)/len(js_quick_tempos):.4f}ms")





# Análise gráfica dos resultados

import numpy as np
import matplotlib.pyplot as plt

     # Calcular média, mediana, desvio padrão
python_bubble_media = np.mean(python_bubble_tempos)
python_bubble_mediana = np.median(python_bubble_tempos)
python_bubble_std = np.std(python_bubble_tempos)

# 2. GRÁFICOS RECOMENDADOS PARA COMPARAÇÃO DE TEMPO:

#    a) GRÁFICO DE BARRAS - Comparação de médias:

algoritmos = ['Python Bubble', 'Python Quick', 'JS Bubble', 'JS Quick']
medias_tempo = [np.mean(python_bubble_tempos), np.mean(python_quick_tempos),
                      np.mean(js_bubble_tempos), np.mean(js_quick_tempos)]

plt.figure(figsize=(10, 6))
plt.bar(algoritmos, medias_tempo, color=['red', 'green', 'orange', 'blue'])
plt.title('Tempo Médio de Execução por Algoritmo')
plt.ylabel('Tempo (ms)')
plt.show()

#    b) BOX PLOT - Mostra distribuição completa dos dados:
dados_tempo = [python_bubble_tempos, python_quick_tempos, js_bubble_tempos, js_quick_tempos]

plt.figure(figsize=(10, 6))
plt.boxplot(dados_tempo, labels=algoritmos)
plt.title('Distribuição dos Tempos de Execução')
plt.ylabel('Tempo (ms)')
plt.show()

#    c) GRÁFICO DE LINHAS - Variação entre execuções:
execucoes = range(1, 11)

plt.figure(figsize=(12, 6))
plt.plot(execucoes, python_bubble_tempos, 'o-', label='Python Bubble', color='red')
plt.plot(execucoes, python_quick_tempos, 's-', label='Python Quick', color='green')
plt.plot(execucoes, js_bubble_tempos, '^-', label='JS Bubble', color='orange')
plt.plot(execucoes, js_quick_tempos, 'd-', label='JS Quick', color='blue')
plt.xlabel('Execução')
plt.ylabel('Tempo (ms)')
plt.title('Variação do Tempo por Execução')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3. GRÁFICOS RECOMENDADOS PARA COMPARAÇÃO DE MEMÓRIA:

#    a) GRÁFICO DE BARRAS AGRUPADAS - Tempo vs Memória:
x = np.arange(len(algoritmos))
width = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

      # Tempo
ax1.bar(algoritmos, medias_tempo, color=['red', 'green', 'orange', 'blue'])
ax1.set_ylabel('Tempo (ms)')
ax1.set_title('Tempo Médio')

      # Memória
medias_memoria = [np.mean(python_bubble_memorias), np.mean(python_quick_memorias),np.mean(js_bubble_memorias), np.mean(js_quick_memorias)]
ax2.bar(algoritmos, medias_memoria, color=['red', 'green', 'orange', 'blue'])
ax2.set_ylabel('Memória (KB)')
ax2.set_title('Memória Média')

plt.tight_layout()
plt.show()

#    b) SCATTER PLOT - Correlação Tempo vs Memória:
todas_medias_tempo = [np.mean(python_bubble_tempos), np.mean(python_quick_tempos), np.mean(js_bubble_tempos), np.mean(js_quick_tempos)]
todas_medias_memoria = [np.mean(python_bubble_memorias), np.mean(python_quick_memorias), np.mean(js_bubble_memorias), np.mean(js_quick_memorias)]

plt.figure(figsize=(8, 6))
cores = ['red', 'green', 'orange', 'blue']
for i, alg in enumerate(algoritmos):
    plt.scatter(todas_medias_tempo[i], todas_medias_memoria[i],
    c=cores[i], s=100, label=alg)

plt.xlabel('Tempo Médio (ms)')
plt.ylabel('Memória Média (KB)')
plt.title('Correlação Tempo vs Memória')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()



def criar_graficos_comparativos():
    # Seus arrays aqui (copie os resultados do teste)

    # Calcular estatísticas
    algoritmos = ['Python Bubble', 'Python Quick', 'JS Bubble', 'JS Quick']
    dados_tempo = [python_bubble_tempos, python_quick_tempos, js_bubble_tempos, js_quick_tempos]
    dados_memoria = [python_bubble_memorias, python_quick_memorias, js_bubble_memorias, js_quick_memorias]

    medias_tempo = [np.mean(dados) for dados in dados_tempo]
    medias_memoria = [np.mean(dados) for dados in dados_memoria]

    # Criar subplot com 4 gráficos
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # 1. Barras - Tempo
    ax1.bar(algoritmos, medias_tempo, color=['#FF6B6B', '#4ECDC4', '#45B7D1', "#B4FD53"])
    ax1.set_title('Tempo Médio de Execução')
    ax1.set_ylabel('Tempo (ms)')

    # 2. Barras - Memória
    ax2.bar(algoritmos, medias_memoria, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#B4FD53'])
    ax2.set_title('Memória Média Utilizada')
    ax2.set_ylabel('Memória (KB)')

    # 3. Box Plot - Tempo
    ax3.boxplot(dados_tempo, labels=[alg.split()[1] for alg in algoritmos])
    ax3.set_title('Distribuição dos Tempos')
    ax3.set_ylabel('Tempo (ms)')

    # 4. Scatter - Tempo vs Memória
    cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#B4FD53']
    for i, alg in enumerate(algoritmos):
        ax4.scatter(medias_tempo[i], medias_memoria[i], c=cores[i], s=150, label=alg)
    ax4.set_xlabel('Tempo (ms)')
    ax4.set_ylabel('Memória (KB)')
    ax4.set_title('Tempo vs Memória')
    ax4.legend()

    plt.tight_layout()
    plt.savefig('analise_comparativa.png', dpi=300, bbox_inches='tight')
    plt.show()

# # Para usar: simplesmente chame criar_graficos_comparativos() após ter os arrays

criar_graficos_comparativos()
# MELHOR ESTRATÉGIA PARA ANÁLISE:
# - Use gráfico de BARRAS para comparação direta de médias
# - Use BOX PLOT para ver consistência e outliers
# - Use SCATTER PLOT para ver correlação tempo/memória
# - Use HEATMAP para visualização normalizada de múltiplas métricas
# """