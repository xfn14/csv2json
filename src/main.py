import re
import sys

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

values = []
for line in csvLines:
    cols = re.split(r',|\n', line)
    cols.pop()
    value = []
    nToSkip = 0
    for i in range(len(headers)):
        if nToSkip != 0:
            nToSkip -= 1
            pass
        if listType[i] == None:
            value.append(cols[i])
        else:
            listSize = re.split(r',', listType[i][0])
            rang = listSize[0] if len(listSize) == 1 else listSize[1]
            nToSkip = rang
            lista = []
            for j in range(int(rang)):
                val = cols[i + j]
                if val != '':
                    lista.append(int(val))
            value.append(lista)
    values.append(value)

# Functions allowed as of the moment of implementation: max, min, avg, sum
def applyFunction(func, l):
    n = len(l)
    res = 0
    
    if func == "sum":
        for i in l:
            res += i
    elif func == "media":
        for i in l:
            res += i
        res /= n
    else:
        res = -1
    return res


with open(re.sub(r'\.csv', ".json", path), "w", encoding="utf-8") as jsonFile:
    if len(values) == 0:
        jsonFile.write("[]\n")
    else:
        jsonFile.write("[\n")
        num = 0
        for val in values:
            jsonFile.write("\t{\n")
            for i in range(len(val)):
                name = headers[i] if listType[i] == None else re.search(r'(.*)\{', headers[i]).groups()[0]
                jsonFile.write("\t\t\"{}\": {}{}\n".format(name, val[i] if type(val[i]) == list or val[i].isnumeric() else "\"{}\"".format(val[i]), "" if i == (len(val) - 1) else ","))
            jsonFile.write("\t{}\n".format("}" if num + 1 == len(values) else "},"))
            num += 1
        jsonFile.write("]\n")







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
#    jsonf.write(json.dumps(value, indent=4))