import re
import sys
import json

path = sys.argv[1]                             # Gets path of .csv file to be converted
csvFile = open(path, "r", encoding="utf-8")    # Open the .csv file for reading
csvLines = csvFile.readlines()                 # Read the lines of .csv file
test = re.compile(r'(?:[^,{.*}]|\{[^)]*\})+')
headers = test.findall(csvLines.pop(0))[:-1]
listType = []

for header in headers:
    if header == '':
        listType.append(None)
        
    val = re.search(r'\{(.*?)\}', header)
    if val == None:
        listType.append(val)
    else:
        func = re.search(r'\:\:(.*)', header)
        if func == None:
            listType.append((val.groups()[0], None))
        else:
            listType.append((val.groups()[0], func.groups()[0]))

print(listType)

for line in csvLines:
    cols = re.split(r',|\n', line)
    cols.pop()
    value = []
    for i in range(len(headers)):
        if listType[i] == None:
            value.append(cols[i])
        else:
            print(listType[i][0])

jsonFile = open(re.sub(r'\.csv', ".json", path), "w", encoding="utf-8")




#Functions allowed as of the moment of implementation: max,min,avg,sum
def applyFunction(func, l):
    n = len(l)
    res = 0
    
    if func == "sum":
        for i in l:
            res += i
    elif func == "media":
        res = applyFunction("Notas_sum",l)/n
    elif func == "max":
        res = max(l)
    elif func == "min":
        res = min(l)
    else:
        res = -1
    return res



#aluno = r'(?:\"(?P<id>.+)\",)(?:\"(?P<nome>.+)\",)(?:\"(?P<curso>.+)\",)(?:(\d+),)(?:(\d+),)(?:(\d+),)(\d+)'
#paluno = re.compile(aluno)
#
#lista = [] 
#
#for linha in sys.stdin:
#    maluno = paluno.search(linha)
#    if maluno:
#        dic = maluno.groupdict()
#        lista.append(dic)
#
#with open("test.json", 'a', encoding='utf-8') as jsonf:
#    jsonf.write(json.dumps(lista, indent=4))