import re
import sys
import json

path = sys.argv[1]
csvFile = open(path, "r")
csvLines = csvFile.readlines()
jsonFile = open(re.sub(r'\.csv', ".json", path), "r")
headers = re.split(r';', csvLines[0])

aluno = r'(?:\"(?P<id>.+)\",)(?:\"(?P<nome>.+)\",)(?:\"(?P<curso>.+)\",)(?:(\d+),)(?:(\d+),)(?:(\d+),)(\d+)'
paluno = re.compile(aluno)

lista = []

for linha in sys.stdin:
    maluno = paluno.search(linha)
    if maluno:
        dic = maluno.groupdict()
        lista.append(dic)

with open("test.json", 'a', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(lista, indent=4))