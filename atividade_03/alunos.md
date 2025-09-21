
## Alunos
ADRIANO DA SILVA JUNIOR
ANTONIO UMBERTO CAMARGO MORI

### Linguagens

- JAVA
- PYTHON
- C##

## Tratativas Implementadas

### 1. Estrutura de Classes (seguindo padrão Java)

**Python:**
- `Node`: Classe para representar os nós da lista duplamente ligada
- `LinkedList`: Classe principal da lista ligada com todos os métodos
- `MaquinaDeLerArquivos`: Classe responsável por ler arquivos e processar comandos
- `main.py`: Arquivo principal de execução

### 2. Tratamento de Valores Não Encontrados na Remoção

**Problema:** Quando um comando `R valor` tenta remover um valor que não existe na lista.

**Solução Implementada:**
- **Java:** Exibe mensagem de aviso "Valor X não encontrado para remoção!" e continua execução
- **Python:** Implementa o mesmo comportamento - exibe mensagem e retorna -1, permitindo continuidade

**Código:**
```python
if current is None:
    print("----------------------------------------------")
    print(f"Valor {value} não encontrado para remoção!")
    print()
    return -1
```

### 3. Modo Debug vs Modo Produção

**Debug Mode (debug_mode = True):**
- Exibe informações detalhadas sobre cada operação
- Mostra lista com índices: `[índice, valor]`
- Imprime mensagens de adição/remoção

**Modo Produção (debug_mode = False):**
- Salva resultados em arquivo `resultado.txt`
- Não exibe informações extras
- Formato de saída limpo para análise

### 4. Salvamento Automático de Resultados

**Tratativa:** Em vez de apenas imprimir na tela, o sistema:
- Captura a saída de cada comando `P` (Print)
- Salva todos os resultados em arquivo `resultado.txt`
- Mantém histórico completo das operações

### 5. Lista Duplamente Ligada

**Implementação:**
- Cada nó tem referências `next` e `previous`
- Mantém referências para `head` e `tail`
- Controla `size` para operações eficientes
- Permite inserção/remoção em qualquer posição

### 6. Tratamento de Índices Inválidos

**Validação:**
```python
if index < 0 or index > self.size:
    raise IndexError("Index inválido")
```

### 7. Listas Grandes (>200 elementos)

**Tratativa:** Para listas com mais de 200 elementos:
- Java/Python: Exibe "Lista muito grande para imprimir!"
- Evita problemas de performance na visualização

### 8. Separação de Responsabilidades

**Arquitetura:**
- `Node`: Apenas estrutura de dados
- `LinkedList`: Lógica da lista ligada
- `MaquinaDeLerArquivos`: Processamento de arquivos e comandos
- `main.py`: Ponto de entrada da aplicação

### 9. Compatibilidade entre Java e Python

**Funcionalidades idênticas:**
- Mesmos métodos e comportamentos
- Mesma lógica de tratamento de erros
- Mesmo formato de saída
- Mesma estrutura de classes (adaptada para Python)