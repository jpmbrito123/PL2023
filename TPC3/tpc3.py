import re
import json


def file_parse(file_path):
    regex_pattern = r"(?P<dir>\d+)::(?P<ano>\d{4})-(?P<mes>\d{2})-(?P<dia>\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<nome_pai>[a-zA-Z ]+)::(?P<nome_mae>[a-zA-Z ]+)::(?P<obs>.*)::"
    regex = re.compile(regex_pattern)
    parsed_list = []

    with open(file_path, 'r') as f:
        for line in f:
            match = regex.search(line)
            if match:
                parsed_list.append(match.groupdict())

    return parsed_list




def primeiroeultimonome(nome_completo):
    primeiro_nome = re.search(r"\b\w+", nome_completo).group()
    sobrenome = re.search(r"\b\w+$", nome_completo).group()
    return primeiro_nome, sobrenome



def processosporano(parsed_list):
    dict_por_ano = {}

    for dicionario in parsed_list:
        ano = dicionario["ano"]
        dict_por_ano[ano] = dict_por_ano.get(ano, 0) + 1

    print("\n\n\n\n")
    print(dict_por_ano)


def seculo_para_intervalo(seculo):
    primeiro_ano = (seculo - 1) * 100 + 1
    ultimo_ano = primeiro_ano + 99

    return primeiro_ano, ultimo_ano


def top5nomes(parsed_list, seculo, nome_id):
    dict_top5_nomes = {}
    for dict in parsed_list:
        if int(dict["ano"]) // 100 + 1 == seculo:
            nome = primeiroeultimonome(dict["nome"])
            if nome[nome_id] not in dict_top5_nomes:
                dict_top5_nomes[nome[nome_id]] = 0

            dict_top5_nomes[nome[nome_id]] += 1

            if dict["nome_pai"]:
                pai = primeiroeultimonome(dict["nome_pai"])
                if pai[nome_id] not in dict_top5_nomes:
                    dict_top5_nomes[pai[nome_id]] = 0

                dict_top5_nomes[pai[nome_id]] += 1

            if dict["nome_mae"]:
                mae = primeiroeultimonome(dict["nome_mae"])
                if mae[nome_id] not in dict_top5_nomes:
                    dict_top5_nomes[mae[nome_id]] = 0

                dict_top5_nomes[mae[nome_id]] += 1

    return sorted(dict_top5_nomes.items(), key=lambda x: x[1], reverse=True)[:5]



def top5seculo(parsed_file):
    first_name = {}
    last_name = {}

    for i in range(1, 22):
        first_name[seculo_para_intervalo(i)] = top5nomes(parsed_file, i, 0)
        last_name[seculo_para_intervalo(i)] = top5nomes(parsed_file, i, 1)

    print("\n\n\n\n")
    print(first_name)
    print("\n\n")
    print(last_name)




def frequencia_parentesco(parsed_file):
    regex1 = re.compile(r",[\w\s]+.[\s*](?i:Proc)|,[\w\s]+.[:]+")
    regex2 = re.compile(r".[\s*](?i:Proc.)")
    dict_parentesco = {}

    for item in parsed_file:
        obs = item.get("obs", "")
        matches = regex1.findall(obs)
        for match in matches:
            pos = match.find(".")
            elem = match[1:pos].strip()
            dict_parentesco[elem] = dict_parentesco.get(elem, 0) + 1

    print("\n\n\n\n")
    print(dict_parentesco)


def convert_to_json(data, output):
    if ".json" not in output:
        output = output + ".json"

    file = open(output, "w")
    file.write("[\n")

    for i in range(min(20, len(data))):
        json.dump(data[i], file, indent=3, separators=(',', ': '))
        if i != min(19, len(data)-1):
            file.write(",\n")
    file.write("\n]")

    file.close()

data = file_parse("./processos.txt")
processosporano(data)
top5seculo(data)
frequencia_parentesco(data)
convert_to_json(data, "jsonfile")
