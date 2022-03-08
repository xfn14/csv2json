import re
import sys
import json

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