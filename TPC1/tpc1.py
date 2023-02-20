import matplotlib.pyplot as plt
total = 0
dados = []
sexos = {"M": 0, "F": 0}
faixas_etarias = dict()
niveis_colesterol = dict()

def parse_file():
    global total
    with open("myheart.csv", "r") as f:
        for line in f.readlines()[1:]:
            total += 1
            dados_pessoa = line[:-1].split(',')
            dados.append(dados_pessoa)

def set_sexos():
    for dado_pessoa in dados:
        if dado_pessoa[1] == 'F':
            if dado_pessoa[5] == '1':
                sexos['F'] += 1
        else:
            if dado_pessoa[5] == '1':
                sexos['M'] += 1

def max_min_idade():
    min_idade = None
    max_idade = None
    for dado_pessoa in dados:
        if min_idade == None or int(dado_pessoa[0]) <= min_idade:
            min_idade = int(dado_pessoa[0])
        if max_idade == None or int(dado_pessoa[0]) >= max_idade:
            max_idade = int(dado_pessoa[0])
    return min_idade, max_idade

def set_faixas_etarias():
    min_idade, max_idade = max_min_idade()
    for idade in [x for x in range(min_idade, max_idade) if x % 5 == 0]:
        faixas_etarias[idade] = 0
        for dado_pessoa in dados:
            if idade <= int(dado_pessoa[0]) <= idade + 4:
                if dado_pessoa[5] == "1":
                    faixas_etarias[idade] += 1

def max_min_colesterol():
    min_colesterol = 0
    max_colesterol = None
    for dado_pessoa in dados:
        if min_colesterol == None or int(dado_pessoa[3]) <= min_colesterol:
            min_colesterol = int(dado_pessoa[3])
        if max_colesterol == None or int(dado_pessoa[3]) >= max_colesterol:
            max_colesterol = int(dado_pessoa[3])
    return min_colesterol, max_colesterol

def set_niveis_colesterol():
    min_colesterol, max_colesterol = max_min_colesterol()
    for nivel in [x for x in range(min_colesterol, max_colesterol) if x % 10 == 0]:
        niveis_colesterol[nivel] = 0
        for dado_pessoa in dados:
            if nivel <= int(dado_pessoa[3]) <= nivel + 9:
                if dado_pessoa[5] == '1':
                    niveis_colesterol[nivel] += 1

def print_table(option, distrbuicao):
    # Print a table with the distribution data
    total = sum(distrbuicao.values())
    x, y = [], []
    for key, value in distrbuicao.items():
        perc = value / total * 100

        if option == 1:
            x.append(key)
            y.append(perc)
            print(f"{key:<20} {perc:.2f}%")
        elif option == 2:
            x.append(f"{key}-{key+4}")
            y.append(perc)
            print(f"{key:<20} {perc:.2f}%")
        elif option == 3:
            x.append(f"{key}-{key+9}")
            y.append(perc)
            print(f"{key:<20} {perc:.2f}%")

    # Create a bar chart with the distribution data
    plt.bar(x, y)
    plt.title('Distribuição de casos de doença cardíaca')
    plt.xlabel('Distribuição')
    plt.ylabel('Percentagem')
    plt.show()

def main():
    parse_file()
    set_sexos()
    set_faixas_etarias()
    set_niveis_colesterol()

    while True:
        print("1 - Percentagem de doentes por sexo")
        print("2 - Percentagem de doentes por grupo etário")
        print("3 - Percentagem de doentes por nível de colestrol")
        print("0 - Sair\n")

        option = input("Select an option: ")
        print()
        if option == '1':
            print_table(1, sexos)
        elif option == '2':
            print_table(2, faixas_etarias)
        elif option == '3':
            print_table(3, niveis_colesterol)
        elif option == '0':
            break
        else:
            print("Opção incorreta, insira novamente\n")

if __name__ == '__main__':
    main()