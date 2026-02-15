# Abrindo o arquivo CSV contendo os dados da "pergunta 3"
with open("../data/incidence_by_sex.csv", "r") as arquivo:
    lista = arquivo.readlines()

# Removendo linhas desnecessárias do início e do final do arquivo (informações que não são dados)
lista = lista[4:-14]

# Criando uma nova lista que armazenará os dados limpos e apenas as colunas importantes
nova_lista = []

for i in lista:
    # Remove quebras de linha e divide cada linha em colunas pelo separador ","
    colunas = i.strip("\n").split('","')
    # Remove aspas de cada valor
    colunas = [c.strip('"') for c in colunas]
    
    # Seleciona apenas as colunas de interesse (Year e Rate) de cada um dos sexos e adiciona à nova lista
    aux = [0,1,5]
    nova_lista.append([colunas[a] for a in aux])

# Criando a lista de nomes das colunas (cabeçalhos) e os sexos para usar como chaves do dicionário
chaves = []
for i in range(0, len(nova_lista[0])):
    chaves.append(" - ".join([nova_lista[0][i], nova_lista[1][i]]))

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
# Taxa observada por 100.000 habitantes no sexo feminino
rate_female = []
# Taxa observada por 100.000 habitantes no sexo masculino
rate_male = []

# Convertendo os dados para tipos numéricos apropriados e adicionando os valores nas listas associadas
for i in dados[chaves[0]]:
    years.append(int(i))

for i in dados[chaves[1]]:
    rate_female.append(float(i))

for i in dados[chaves[2]]:
    rate_male.append(float(i))

# Imprimindo os dados para conferência
for i in range(0, len(years)):
    print("Year:", years[i], "Rate female:", rate_female[i], "Rate male:", rate_male[i])

# Função que calcula a média de uma lista
def media(lista):
    return round(sum(lista) / len(lista), 2)

# Imprimindo as médias da taxa de incidência por sexo
print("\nMédia:")
print("Rate female:", media(rate_female), "Rate male:", media(rate_male))

# Função que calcula a variação percentual entre o primeiro e último ano
def variacao(rate_inicial, rate_final):
    return round(((rate_final - rate_inicial) / rate_inicial) * 100, 2)

# Imprimindo a variação percentual da taxa observada por sexo
print("\nVariação:")
print("Rate female:", variacao(rate_female[0], rate_female[-1]), "Rate male:", variacao(rate_male[0], rate_male[-1]))

# Importando o módulo matplotlib para visualização gráfica
import matplotlib.pyplot as plt

plt.figure()

# Plotando a linha da taxa observada do sexo feminino
plt.plot(years, rate_female, label="feminino")

# Plotando a linha da taxa observada do sexo masculino 
plt.plot(years, rate_male, label="masculino")

# Configurando os rótulos e título do gráfico
plt.xlabel("Ano")
plt.ylabel("Taxa por 100.000")
plt.title("Tendência da Incidência de Câncer")

# Exibindo as legendas de cada linha
plt.legend()

# Exibindo o gráfico
plt.show()

