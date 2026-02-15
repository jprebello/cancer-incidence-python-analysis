# Abrindo o arquivo CSV contendo os dados da "pergunta 1"
with open("../data/incidence_over_time.csv", "r") as arquivo:
    lista = arquivo.readlines()

# Removendo linhas desnecessárias do início e do final do arquivo (informações que não são dados)
lista = lista[5:-14]

# Criando uma nova lista que armazenará os dados limpos e apenas as colunas importantes
nova_lista = []

for i in lista:
    # Remove quebras de linha e divide cada linha em colunas pelo separador ","
    colunas = i.strip("\n").split('","')
    # Remove aspas de cada valor
    colunas = [c.strip('"') for c in colunas]
    
    # Seleciona apenas as colunas de interesse (Year, Rate e Modeled Rate) e adiciona à nova lista
    aux = [0,1,4]
    nova_lista.append([colunas[a] for a in aux])

# Criando a lista de nomes das colunas (cabeçalhos) para usar como chaves do dicionário
chaves = []
for i in nova_lista[0]:
    chaves.append(i)

# Inicializando o dicionário que armazenará os dados organizados por colunas
dados = dict()

# Preenchendo as chaves do dicionário
for i in chaves:
    dados[i] = []

# Preenchendo o dicionário com os valores de cada coluna
for i in nova_lista[1:]:
    for j in range(0, len(i)):
        dados[chaves[j]].append(i[j])

# Criando listas separadas para cada coluna que será usada na análise
# Anos de diagnóstico
years = []
# Taxa observada por 100.000 habitantes
rate = []
# Taxa modelada (linha de tendência)
modeled_rate = []

# Convertendo os dados para tipos numéricos apropriados e adicionando os valores nas listas associadas
for i in dados["Year of Diagnosis"]:
    years.append(int(i))

for i in dados["Rate per 100,000"]:
    rate.append(float(i))

for i in dados["Modeled Rate (Trend Line)"]:
    modeled_rate.append(float(i))

# Imprimindo os dados para conferência
for i in range(0, len(years)):
    print("Year:", years[i], "Rate:", rate[i], "Modeled Rate:", modeled_rate[i])

# Calculando a variação percentual da taxa observada entre o primeiro e o último ano
taxa_variacao = 0.0

taxa_variacao = ( (rate[-1] - rate[0]) / rate[0] ) * 100

print("Taxa de variação:", round(taxa_variacao, 1))

# Calculando a diferença absoluta da taxa modelada entre o primeiro e o último ano
diferenca = 0.0

diferenca = modeled_rate[-1] - modeled_rate[0]

print("Diferença:", round(diferenca, 1))

# Importando o módulo matplotlib para visualização gráfica
import matplotlib.pyplot as plt

plt.figure()

# Plotando a linha da taxa observada
plt.plot(years, rate, label="taxa de incidência")

# Plotando a linha da tendência (modeled rate)
plt.plot(years, modeled_rate, label="taxa modelada")

# Configurando os rótulos e título do gráfico
plt.xlabel("Ano")
plt.ylabel("Taxa por 100.000")
plt.title("Tendência da Incidência de Câncer")

# Exibindo as legendas de cada linha
plt.legend()

# Exibindo o gráfico
plt.show()

