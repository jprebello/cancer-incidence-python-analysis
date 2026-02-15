# Abrindo o arquivo CSV contendo os dados da "pergunta 2"
with open("../data/incidence_by_age.csv", "r") as arquivo:
    lista = arquivo.readlines()

# Removendo linhas desnecessárias do início e do final do arquivo (informações que não são dados)
lista = lista[4:-14]

# Convertendo &lt; em <
lista[0] = lista[0].replace("&lt;", "<")

# Criando uma nova lista que armazenará os dados limpos e apenas as colunas importantes
nova_lista = []

for i in lista:
    # Remove quebras de linha e divide cada linha em colunas pelo separador ","
    colunas = i.strip("\n").split('","')
    # Remove aspas de cada valor
    colunas = [c.strip('"') for c in colunas] 

    # Seleciona apenas as colunas de interesse (Year e Rate) de cada uma das faixa etárias e adiciona à nova lista
    aux = [0,1,5,9,13,17]
    nova_lista.append([colunas[a] for a in aux])

# Criando a lista de nomes das colunas (cabeçalhos) e as faixa etárias para usar como chaves do dicionário
chaves = []
for i in range(0, len(nova_lista[0])):
    chaves.append(" - ".join([nova_lista[0][i],nova_lista[1][i]]))

# Removendo os primeiros caracteres da chave Year of Diagnosis
chaves[0] = chaves[0].lstrip(" -")

# Inicializando o dicionário que armazenará os dados organizados por colunas
dados = dict()

# Preenchendo as chaves do dicionário
for i in chaves:
    dados[i] = []

# Preenchendo o dicionário com os valores de cada coluna
for i in nova_lista[2:]:
    for j in range(0, len(i)):
        dados[chaves[j]].append(i[j])

# Criando listas separadas para cada coluna que será usada na análise
# Anos de diagnóstico
years = []
# Taxa observada por 100.000 habitantes na faixa <15 anos
rate_menor_15 = []
# Taxa observada por 100.000 habitantes na faixa 15-39 anos
rate_15_39 = []
# Taxa observada por 100.000 habitantes na faixa 40-64 anos
rate_40_64 = []
# Taxa observada por 100.000 habitantes na faixa 65-74 anos
rate_65_74 = []
# Taxa observada por 100.000 habitantes na faixa >75 anos
rate_maior_75 = []

# Convertendo os dados para tipos numéricos apropriados e adicionando os valores nas listas associadas
for i in dados[chaves[0]]:
    years.append(int(i))

for i in dados[chaves[1]]:
    rate_menor_15.append(float(i.replace(",", "")))

for i in dados[chaves[2]]:
    rate_15_39.append(float(i.replace(",", "")))
    
for i in dados[chaves[3]]:
    rate_40_64.append(float(i.replace(",", "")))

for i in dados[chaves[4]]:
    rate_65_74.append(float(i.replace(",", "")))

for i in dados[chaves[5]]:
    rate_maior_75.append(float(i.replace(",", "")))

# Imprimindo os dados para conferência
for i in range(0, len(years)):
    print("Year:", years[i], "Rate <15:", rate_menor_15[i], "Rate 15-39:", rate_15_39[i], "Rate 40-64:", rate_40_64[i], "Rate 65-74:", rate_65_74[i], "Rate 75+:", rate_maior_75[i])

# Função que calcula a média de uma lista
def media(lista):
    return round(sum(lista) / len(lista), 2)

# Imprimindo as médias da taxa de incidência por faixa etária
print("\nMédia:")
print("Rate <15:", media(rate_menor_15), "Rate 15-39:", media(rate_15_39), "Rate 40-64:", media(rate_40_64), "Rate 65-74:", media(rate_65_74), "Rate 75+:", media(rate_maior_75))

# Função que calcula a variação percentual entre o primeiro e último ano
def variacao(rate_inicial, rate_final):
    return round(((rate_final - rate_inicial) / rate_inicial) * 100, 2)

# Imprimindo a variação percentual da taxa observada por faixa etária
print("\nVariação:")
print("Rate <15:", variacao(rate_menor_15[0], rate_menor_15[-1]), "Rate 15-39:", variacao(rate_15_39[0], rate_15_39[-1]), "Rate 40-64:", variacao(rate_40_64[0], rate_40_64[-1]), "Rate 65-74:", variacao(rate_65_74[0], rate_65_74[-1]), "Rate 75+:", variacao(rate_maior_75[0], rate_maior_75[-1]))

# Importando o módulo matplotlib para visualização gráfica
import matplotlib.pyplot as plt

plt.figure()

# Plotando a linha da taxa observada da faixa <15
plt.plot(years, rate_menor_15, label="<15 anos")

# Plotando a linha da taxa observada da faixa 15-39 
plt.plot(years, rate_15_39, label="15-39 anos")

# Plotando a linha da taxa observada da faixa 40-64 
plt.plot(years, rate_40_64, label="40-64 anos")

# Plotando a linha da taxa observada da faixa 65-74
plt.plot(years, rate_65_74, label="65-74 anos")

# Plotando a linha da taxa observada da faixa 75+ 
plt.plot(years, rate_maior_75, label="75+ anos")

# Configurando os rótulos e título do gráfico
plt.xlabel("Ano")
plt.ylabel("Taxa por 100.000")
plt.title("Tendência da Incidência de Câncer")

# Exibindo as legendas de cada linha
plt.legend()

# Exibindo o gráfico
plt.show()
