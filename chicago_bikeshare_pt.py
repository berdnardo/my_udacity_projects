# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
lines = 0
for types in range(0, 20):
    lines += 1
    data = list(data_list[lines])
    print(data)
# Vamos mudar o data_list para remover o cabeçalho dele.
#   *exclui essa linha de comando
# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]
input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
gender = []
for count in range(1, 21):
    count += 1
    gender_count = list(zip(data_list[0], data_list[count]))
    gender.append(gender_count[6])
print(gender)
# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista

def column_to_list(data, index):
    """Função de criação de lista iterando uma coluna de uma lista principal
    Parametros de entrada:
    Parametro 1: lista a ser iterada para aquisição dos itens para a criação de uma nova lista.
    Parametro 2: index que corresponde ao item da lista principal a ser criado uma nova lista.
    A função retorna uma lista de um item especifico de uma lista principal.
    """
    column_list = []
    data = data_list[1:]
    for column in data:
        column_list.append(column[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

male = 0
female = 0
for gender in data_list:
    if 'Male' in gender:
        male += 1
    elif 'Female' in gender:
        female+= 1
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

def count_gender(data_list):
    """Função que faz a contegem de quantas str 'Male' e 'Female' existem dentro da lista data_list
        Parametro de entrada:
        parametro fixo lista data_list
        Retorna duas variaveis male e female com o total da contagem da str 'Male' 'Female'.
        """
    male = 0
    female = 0
    for gender in data_list:
        if 'Male' in gender:
            male += 1
        elif 'Female' in gender:
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.

def most_popular_gender(data_list):
    """Função que faz a contagem dos dos generos da lista data_list e retorna a maior ocorrencia
        Parametro:
            parametro fixo data_list
    Retorna valor como str da maior ocorrencia, no caso de igualdade retorna str 'Igual'
    """
    answer = ""
    for data in data_list:
        male = 0
        female = 0
        if 'Male' in data:
            male += 1
        elif 'Female' in data:
            female += 1
    if male > female:
        answer = str('Male')
    elif male < female:
        answer = str('Female')
    else:
        answer = str('Igual')
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_types(data_list):
    """Função que faz a contagem dos tipos de usuarios da lista data_list
        Parametro:
            parametro fixo data_list
        Retorna valor como int do total de tipos de usuarios.
    """
    subscriber = 0
    customer = 0
    for data in data_list:
        if 'Subscriber' in data:
            subscriber += 1
        elif 'Customer' in data:
            customer += 1
    return [subscriber, customer]

user_types_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque a funçao len soma todos os itens da lista, enquanto o outro lado da igualdade é o somatório de alguns itens dentro dessa lista."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
#data_list = data_list[1:]
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
#criando uma lista convertendo as strings em intenger.
time_trip = []
for duration in trip_duration_list:
    time_trip.append(int(duration))
time_trip.sort()
#função utilizada para auxiliar o calculo da media e mediana.
total_duration = 0
total_trips = 0
for count_time in time_trip:
    if count_time:
        total_duration += count_time
        total_trips += 1
median_index_1= total_trips/2
median_index_2= total_trips/2+1
main_index= int((median_index_1+median_index_2)/2)
#resultado das variaveis
min_trip = time_trip[0]
max_trip = time_trip[-1]
mean_trip = round(total_duration/total_trips)
median_trip = time_trip[main_index] #fazer (xn/2+xn/2+1)/2 calculo base da mediana.


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

user_types = set(column_to_list(data_list,3))
print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
    Função de exemplo com anotações.
            Argumentos:
            param1: O primeiro parâmetro.
            param2: O segundo parâmetro.
            Retorna:
            Uma lista de valores x.
"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)

# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"


def count_items(column_list):
    """Função que gera duas listas uma com os tipos de dados sem a repetição dos itens e outra que conta o total de itens
        dentro dessa mesma lista.
        Parametro:
            usa como parametro outra função column_list para pegar uma coluna especifica dentro de uma lista
        Retorna lista item_types com o itens da lista principal sem repetição e a lista count_items com o total de itens
        dentro da lista principal.
    """
    things = 0
    item_types = set(column_list)
    count_items=[]
    for types in column_list:
        if '' in types:
            things += 1
    count_items.append(things)
    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------