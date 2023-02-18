list_1 = []
list_2 = []
file_name_1 = '1.txt'
file_name_2 = '2.txt'

with open(file_name_1, 'r', encoding='UTF-8') as f:
    list_1.append(f.readlines())

with open(file_name_2, 'r', encoding='UTF-8') as f:
    list_2.append(f.readlines())

with open('result.txt', 'w', encoding='UTF-8') as f:
    if len(list_1[0]) <= len(list_2[0]):
        f.write(file_name_1 + '\n')
        f.write(str(len(list_1[0])) + '\n')
        for i in range(len(list_1[0])):
            f.write(list_1[0][i])
        f.write('\n' + file_name_2 + '\n')
        f.write(str(len(list_2[0])) + '\n')
        for i in range(len(list_2[0])):
            f.write(list_2[0][i])
    else:
        f.write(file_name_2 + '\n')
        f.write(str(len(list_2[0])) + '\n')
        for i in range(len(list_2[0])):
            f.write(list_2[0][i])
        f.write('\n' + file_name_1 + '\n')
        f.write(str(len(list_1[0])) + '\n')
        for i in range(len(list_1[0])):
            f.write(list_1[0][i])
