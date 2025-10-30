### 1. Código-Fonte

*   **Simulação N:M**: `src/TestNM.java`
*   **Simulação 1:1**: `src/Test11.java`
*   **Tarefa Computacional**: `src/Task.java` (Usada por ambas as simulações)

### 2. Tabela de Tempos de Execução

| Quantidade de Tarefas/Threads | Modelo N:M (12 threads) | Modelo 1:1 (1 thread por tarefa) |
| ----------------------------- | ----------------------- | -------------------------------- |
| 10                            | 16 ms                   | 11 ms                            |
| 100                           | 93 ms                   | 18 ms                            |
| 500                           | 429 ms                  | 50 ms                            |
| 1000                          | 857 ms                  | 78 ms                            |

### 3. Relatório com Análise Crítica dos Resultados

#### Análise de Desempenho

*   **Modelo N:M (Thread Pool)**: Apresentou tempo de execução mais lento devido à limitação de 12 threads processando todas as tarefas sequencialmente. Com 1000 tarefas e 12 threads, o tempo teórico mínimo seria ~834ms (1000 ÷ 12 × 10ms), e o resultado real de 857ms está próximo desse valor.

*   **Modelo 1:1**: Demonstrou desempenho superior em tempo total de execução, executando todas as tarefas em paralelo. O tempo permaneceu próximo de 10ms (o tempo de uma única tarefa) mais overhead de criação de threads.

#### Trade-offs e Limitações

Apesar da vitória em velocidade do modelo 1:1, a análise não estaria completa sem considerar seus custos e limitações:

1.  **Consumo de Recursos**: O modelo 1:1 é extremamente caro em recursos. Cada thread do sistema operacional requer sua própria pilha de memória (geralmente ~1MB). Com 1.000 threads. O modelo N:M usa apenas 12 threads, mantendo o consumo de memória baixo e previsível.

2.  **Sobrecarga de Criação de Threads**: Os tempos crescentes do modelo 1:1 (11ms → 78ms) revelam o custo de criar threads. Com 10 threads, o overhead é apenas 1ms; com 1000 threads, sobe para 68ms. O modelo N:M evita esse problema criando threads apenas uma vez no início.

#### Conclusão

O modelo 1:1 vence em velocidade bruta para tarefas de I/O curtas, mas o modelo N:M é a escolha correta para aplicações de produção devido à eficiência de recursos, escalabilidade e previsibilidade de desempenho.
