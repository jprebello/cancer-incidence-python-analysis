# Análise da incidência de câncer nos EUA (Python)

## Base de Dados
- **Descrição:** Conjunto de dados contendo informações sobre a incidência de câncer em 8 grandes regiões dos Estados Unidos, representando aproximadamente **34% da população norte-americana**.
- **Fonte:** SEER – Surveillance, Epidemiology, and End Results Program
- **Ferramenta:** Python

O SEER é um programa federal de pesquisa científica dos Estados Unidos, parte de uma iniciativa governamental de vigilância epidemiológica. Ele coleta informações detalhadas sobre todos os diagnósticos de câncer, incluindo dados hospitalares, laboratoriais, registros de patologia e certificados de óbito, utilizando registros populacionais contínuos de câncer.

Devido à sua ampla cobertura, diversidade racial, socioeconômica e geográfica, e padrão científico consolidado, os dados do SEER permitem inferir tendências populacionais com alta confiabilidade e são amplamente utilizados em estudos epidemiológicos nos Estados Unidos.

## Objetivo do projeto
Tentar responder algumas perguntas relacionadas ao risco de diagnóstico de câncer ao longo do período de 1975 a 2022, bem como às diferenças de incidência entre diferentes faixa etárias e sexos na população norte-americana.

Taxa de incidência: A taxa de incidência por 100.000 habitantes representa o número de novos casos de câncer dividido pelo tamanho da população e multiplicado por 100.000. Essa padronização permite comparar o risco de diagnóstico ao longo do tempo, independentemente do crescimento populacional.

Ajuste por idade: Como o risco de câncer varia fortemente com a idade, as taxas foram ajustadas utilizando a população padrão dos EUA do ano 2000. Esse procedimento aplica pesos fixos às diferentes faixas etárias, permitindo comparações temporais sem distorções causadas pelo envelhecimento da população.

## Estrutura
- data
    - incidence_over_time.csv
    - incidence_by_age.csv
    - incidence_by_sex.csv
- analysis
    - 01_trend_analysis.py
    - 02_age_group_analysis.py
    - 03_sex_analysis.py

## Variáveis utilizadas
1. Year of Diagnosis: Ano em que o câncer foi diagnosticado.

2. Rate per 100.000: Taxa anual de incidência ajustada por idade, expressa por 100.000 habitantes.

3. Modeled Rate (Trend Line): Estimativa estatística suavizada da taxa de incidência ao longo do tempo, reduzindo oscilações anuais aleatórias e permitindo identificar a tendência estrutural.

*O ano de 2020 apresenta uma queda abrupta na taxa de incidência. Isso ocorre devido a pandemia de COVID-19, onde houve redução de exames preventivos, de consultas médicas e um atraso nos diagnísticos.*

# A taxa de incidência de câncer aumentou ao longo dos anos?

## Análise:
Calculando a variação da taxa de incidência entre o ano inicial (1975) e o ano final (2022), observamos:

Taxa observada: **aumento de 15,7%**.

Taxa modelada: **aumento absoluto de 65,4**.

Esses resultados indicam que, considerando apenas o primeiro e o último ano, o risco de diagnóstico de câncer realmente **aumentou** no período analisado.

## Observações do gráfico:

Houve aumento consistente da incidência até aproximadamente **1990**.

Entre **1990 e 2010**, ocorreram oscilações, mas a taxa permaneceu relativamente **estável**, possivelmente refletindo melhorias em diagnósticos e tratamentos.

A partir de **2010**, observa-se **novo aumento** na taxa de incidência, que pode estar associado a fatores como: mudanças nos hábitos de vida da população e maior exposição a fatores de risco.

## Conclusão:
A análise sugere que a incidência de câncer nos EUA **aumentou ao longo do período**, com diferentes fases de crescimento e estabilização. A tendência geral indica que o risco de diagnóstico tem aumentado, especialmente nas últimas décadas, refletindo tanto fatores biológicos quanto socioambientais.

# Como o risco de diagnóstico de câncer varia entre diferentes faixas etárias?

## Análise:
A análise demonstra que a incidência de câncer nos EUA é **significativamente maior** nas **faixas etárias mais avançadas**, especialmente em indivíduos com **75 anos ou mais**. A diferença de risco entre indivíduos acima de 75 anos e jovens abaixo de 15 anos é expressiva, chegando a ser aproximadamente **150 vezes** maior.

Observa-se um crescimento progressivo da taxa de incidência conforme a idade aumenta, com um salto mais acentuado a partir dos **65 anos**.

Além disso, ao comparar os anos de **1975 e 2022**, nota-se que todas as faixas etárias apresentaram aumento na taxa de incidência. O crescimento percentual foi mais expressivo entre os jovens (**43%** em menores de 15 anos e **37%** entre 15 e 39 anos), embora as taxas absolutas permaneçam muito inferiores às observadas em idades mais avançadas.

## Conclusão:
Esses resultados sugerem que o risco de diagnóstico de câncer está fortemente associado ao **envelhecimento**, mas também indicam um aumento estrutural da incidência ao longo do tempo em todas as faixas etárias. Refletindo mudanças recentes nos hábitos e na qualidade de vida das pessoas, principalmente dos mais jovens.

# Homens ou mulheres apresentam maior taxa de incidência?

## Análise:
A análise demonstra que a incidência de câncer nos EUA é significativamente **maior entre os homens**. A diferença, na média, é de cerca de **120 pontos absolutos**.

Além disso, nota-se um crescimento da taxa de incidência, principalmente nas mulheres, ao comparar o ano inicial e final. Esse crescimento é de cerca de **21%** para mulheres e de apenas **6%** para os homens.

## Observações do gráfico:

A taxa dos homens subiu muito até 1990, desde esse período ela encontra-se em decadência. Diferente da taxa das mulheres, que encontra-se subindo desde o ano inicial, com oscilações naturais.

## Conclusão:
Os resultados indicam que a taxa de incidência de câncer é historicamente maior entre os homens. No entanto, observa-se que o crescimento percentual ao longo do período analisado foi mais expressivo entre as mulheres. Esse padrão demonstra uma **redução na diferença** relativa entre os sexos ao longo do tempo. Isso pode ser efeito do envelhecimento populacional associado a uma maior expectativa de vida das mulheres. O crescimento percentual mais acentuado entre as mulheres pode indicar uma tendência de convergência das taxas no futuro.
