import codecs

file1 = "resource/1Cv7 - АРМ SQL.DDS"
file2 = "resource/1Cv7 - АРМ SQL new vers.DDS"

version1 = codecs.open(file1, "r", "cp1251")
version2 = codecs.open(file2, "r", "cp1251")
result = ""

table_name = ""
table_content = ""
dict = {}

while True:
    line = version1.readline()
    if line.startswith("#==TABLE"):
        dict.update({table_name: table_content})
        table_content = ""
        table_name = (line.split(":")[1].strip())
    else:
        table_content += line

    if not line:
        break

# for key, value in dict.items():
#     print(key + "\n" + value + "\n\n\n\n\n")