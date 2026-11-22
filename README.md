# Superfícies paramétricas em Python

Atividade do Tema 6 do Seminário 3 de Computação Gráfica 3D. O objetivo é demonstrar como fórmulas paramétricas geram superfícies tridimensionais e como a quantidade de amostras interfere na aparência da malha.

O programa gera uma esfera, um cilindro ou um cone. O NumPy combina valores de dois parâmetros e calcula as coordenadas `X`, `Y` e `Z` de cada ponto. O Matplotlib usa essas coordenadas para desenhar a superfície em 3D.

| Superfície | Parâmetros usados na fórmula | Como a forma é gerada |
| --- | --- | --- |
| Esfera | Dois ângulos | Um ângulo percorre a volta e o outro vai de um polo ao outro. |
| Cilindro | Ângulo e altura | O raio é constante ao longo da altura. |
| Cone | Ângulo e altura | O raio começa em 1 na base e diminui até zero na ponta. |

O cilindro e o cone representam as superfícies laterais, com as aberturas das bases visíveis.

## Como executar

Com o Python 3 instalado, abra o terminal na pasta do repositório, instale as dependências e execute o arquivo.

```bash
python -m pip install numpy matplotlib
python 06_Superficies_Parametricas.py
```

O script abre uma janela com o gráfico 3D. A configuração inicial usa a esfera com 36 segmentos.

## Experimento proposto

No início do arquivo, use `objeto` para escolher `'esfera'`, `'cilindro'` ou `'cone'`. Use `segmentos` para ajustar a resolução da malha.

1. Escolha uma forma e execute o programa com 8, 16, 36 e 72 segmentos, um valor por vez. Observe a borda e as faces pelo mesmo ângulo de visão.
2. Compare pelo menos duas superfícies. Por exemplo, teste o cilindro e o cone com o mesmo valor de `segmentos` e observe como o raio varia ao longo da altura.
3. Relacione os resultados à modelagem 3D. Com poucas amostras, as faces são mais perceptíveis. Com mais amostras, a malha acompanha melhor a curvatura.
