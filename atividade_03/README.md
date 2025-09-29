# Análise de Performance: Python vs Go

## Resumo dos Testes

Este projeto compara a performance de algoritmos de ordenação implementados em Python e Go com 30.000 números.

## Resultados

### Bubble Sort
- **Python**: ~10-30 minutos
- **Go**: ~3-5 segundos
- **Diferença**: Go é 100-400x mais rápido

### Quick Sort
- **Python**: Alguns segundos
- **Go**: Menos de 1 segundo
- **Diferença**: Go é 5-10x mais rápido

## Por que essas diferenças?

### Python vs Go
- **Go**: Compilado para código nativo
- **Python**: Interpretado, maior overhead

### Bubble Sort vs Quick Sort
- **Bubble Sort**: O(n²) - 900 milhões de operações
- **Quick Sort**: O(n log n) - 450 mil operações
- **Diferença**: Quick Sort é ~2000x mais eficiente

## Conclusão

1. **Linguagem importa**: Go supera Python em performance bruta
2. **Algoritmo importa mais**: Quick Sort vs Bubble Sort faz diferença maior que a linguagem
3. **Para tarefas intensivas**: Use linguagens compiladas + algoritmos eficientes