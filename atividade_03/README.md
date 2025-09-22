# LinkedList Performance Benchmark

Este projeto implementa uma estrutura de dados de lista ligada em três linguagens diferentes (Java, Python, e JavaScript) e compara o desempenho entre elas.


## Funcionalidades Implementadas

### Estrutura de Lista Ligada
- **Node**: Classe que representa um nó da lista com valor, ponteiro para próximo e anterior
- **LinkedList**: Implementa lista duplamente ligada com operações:
  - `addFirst()` - Adiciona elemento no início
  - `addLast()` - Adiciona elemento no final
  - `addAt(index, value)` - Adiciona elemento em posição específica
  - `removeFirst()` - Remove primeiro elemento
  - `removeLast()` - Remove último elemento
  - `removePrimeiroEncontrado(value)` - Remove primeira ocorrência do valor
  - `printList()` - Imprime a lista
  - `printListIndex()` - Imprime lista com índices

### Máquina de Ler Arquivos
- Lê arquivo de entrada com valores iniciais e operações
- Executa operações sequencialmente:
  - `A num pos` - Adiciona número na posição
  - `R num` - Remove primeira ocorrência do número
  - `P` - Imprime a lista
  - `S` - Salva lista em arquivo

## Como Executar

### Executar Implementações Individuais

**Java:**
```bash
cd Java
javac *.java
java Main
```

**Python:**
```bash
cd Python
python main.py
```

**JavaScript:**
```bash
cd JavaScript
node main.js
```

