### 1. Código-Fonte

*   **Simulação N:1**: `src/TestN1.java`
*   **Simulação 1:1**: `src/Test11.java`
*   **Tarefa Computacional**: `src/Task.java` (Usada por ambas as simulações)

### 2. Tabela de Tempos de Execução

| Quantidade de Tarefas/Threads | Modelo N:1 (Tempo Total) | Modelo 1:1 (Tempo Total) |
| ----------------------------- | ------------------------ | ------------------------ |
| 10                            | 104 ms                   | 7 ms                     |
| 100                           | 839 ms                   | 66 ms                    |
| 500                           | 1667 ms                  | 474 ms                   |
| 1000                          | 3134 ms                  | 1013 ms                  |

### 3. Relatório com Análise Crítica dos Resultados

#### Análise de Desempenho

*   **Modelo N:1**: Apresentou um tempo de execução total significativamente mais lento para cargas de trabalho que podem ser paralelizadas.


*   **Modelo 1:1**: Apresentou um desempenho de tempo de execução total drasticamente superior


#### Trade-offs e Limitações

Apesar da vitória em velocidade do modelo 1:1, a análise não estaria completa sem considerar seus custos e limitações, que não são aparentes apenas no tempo de execução:

1.  **Consumo de Recursos**: O modelo 1:1 é caro em termos de memória. Cada thread do sistema operacional requer sua própria pilha de memória (geralmente ~1MB). Com 1.000 threads, isso já representa um consumo de ~1GB de RAM apenas para as pilhas, antes mesmo de a aplicação alocar memória para outros objetos. O modelo N:1, por outro lado, é extremamente leve, usando apenas uma thread e uma pilha.

2.  **Sobrecarga de Contexto (Context Switching)**: Quando o número de threads ativas excede o número de núcleos de CPU disponíveis, o sistema operacional é forçado a alternar rapidamente entre as threads. Essa troca de contexto é uma operação de que causa muito overhead. Isso explica por que o desempenho do modelo 1:1 não escala perfeitamente e a eficiência diminui à medida que o número de threads aumenta.
