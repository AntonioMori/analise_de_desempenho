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