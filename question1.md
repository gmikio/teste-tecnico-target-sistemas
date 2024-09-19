
## Questão 1: Qual será o valor da variável SOMA?

### Código:

```c
int INDICE = 12, SOMA = 0, K = 1;

while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}

printf("%d\n", SOMA);
```

### O valor da variável soma será 77, visto que o código realiza um loop e soma o valor de K a cada iteração, iniciando no 2 e terminando no 12.