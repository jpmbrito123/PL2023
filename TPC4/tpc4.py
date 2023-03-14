import re


def read_csv(filename):
    file = open(filename, "r", encoding="utf-8")
    lines = file.read().split('\n')
    headLine = re.findall(r"(\w+(?:{\d+}(?:::(?:\w)+)*|{\d+,\d+}(?:::(?:\w)+)*)*)", lines[0])
    listDicts = []

    for line in lines[1:]:
        line = line.split(",")
        dictL = {}
        for i in range(0, len(headLine)):
            if headLine[i] != '':
                search = re.search(r'(\w+){(\d+),*(\d*)}', headLine[i])

                if search:
                    valueS = search.group(1)
                    maxValues = int(search.group(2))
                    minValues = i
                    if search.group(3):
                        minValues = maxValues
                        maxValues = int(search.group(3))

                    valuesAux = []

                    for x in range(i, i + maxValues):
                        if line[x] != '':
                            valuesAux.append(line[x])

                    searchFunc = re.search(r'(\w+){(\d+),*(\d*)}::(\w+)', headLine[i])
                    function = ''
                    valuesResult = 0
                    if searchFunc:
                        function = searchFunc.group(3)
                        if searchFunc.group(4) != '':
                            function = searchFunc.group(4)

                        valueS = searchFunc.group(1) + "_" + function
                        if function == "sum":
                            valuesAux = list(map(int, valuesAux))
                            valuesResult = sum(valuesAux)
                        if function == "media":
                            valuesAux = list(map(int, valuesAux))
                            valuesResult = sum(valuesAux) / len(valuesAux)

                    if function != '':
                        dictL[valueS] = str(valuesResult)
                    else:
                        dictL[valueS] = valuesAux

                else:
                    dictL[headLine[i]] = line[i]

        listDicts.append(dictL)

    return listDicts


def json(list_i, path):
    pagjson = "["
    for dict in list_i:
        pagjson += """
            {\n"""

        for i in dict.keys():
            if type(dict[i]) is not list:
                value = dict[i]
                if (not value.isdigit()):
                    value = f""" "{value}" """
                pagjson += f"""           "{i}":{value},\n"""
            else:
                pagjson += f"""           "{i}":["""
                for value in dict[i]:
                    if (not value.isdigit()):
                        value = f"""    "{value}" """
                    pagjson += f"{value},"
                pagjson = pagjson[:-1]
                pagjson += "],\n"

        pagjson = pagjson[:-2]
        pagjson += """
        },"""

    pagjson = pagjson[:-1]
    pagjson += """
    ]"""

    file = open(path + ".json", "w", encoding="utf-8")
    file.write(pagjson)
    file.close()


def main():
    path = "alunos5.csv"
    set = read_csv(path)
    json(set, path.split(".")[0])


if __name__ == '__main__':
    main()
