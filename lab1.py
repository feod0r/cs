# coding=utf-8
import re
import time
import collections
import operator

start_time = time.time()

shift = "дюмях"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # [chr(i) for i in range(1072, 1072+32)]
bigram = []
dict = alphabet
reg_ex = re.compile('[^а-яА-Я ]')

file = open("v i mir.txt", "r", encoding="utf-8")
text = file.read()

print(list(alphabet))

for chr in list(shift):
    dict = dict.replace(chr, '')

# создание словаря с заданным правилом
dict = shift + dict
print(list(dict), len(alphabet), len(dict))



# удаление некириллических символов
text_orig = reg_ex.sub('', text).lower()
text_code = ""

# for i,char in enumerate(dict):
#     text_code = text_code.replace(alphabet[i],char)

# кодирование текста
for char in text_orig:
    if char == " ":
        text_code += " "
    else:
        text_code += dict[alphabet.find(char)]

orig_dict = {}
code_dict = {}
per_orig_dict = {}
per_code_dict = {}
# подсчет количества символов
for i in range(0, len(dict)):
    orig_dict[alphabet[i]] = text_orig.count(alphabet[i])
    code_dict[dict[i]] = text_code.count(alphabet[i])
    per_orig_dict[alphabet[i]] = text_orig.count(alphabet[i]) / len(text_orig)
    per_code_dict[dict[i]] = text_code.count(dict[i]) / len(text_code)
    # print(alphabet[i].ljust(3), " | ",
    #       str(text_orig.count(alphabet[i])).ljust(6),
    #       " | ", str(text_code.count(alphabet[i])).ljust(6),
    #       " | ", str(text_code.count(dict[i])).ljust(6),
    #       dict[i].ljust(3))

print(orig_dict)
print(code_dict)
print(per_orig_dict)
print(per_code_dict)

# вывод процентных значений
# print()
# for i in range(0, len(dict)):
#     print(alphabet[i].ljust(3),
#           " | ", str(round(text_orig.count(alphabet[i]) / len(text_orig), 4)).ljust(6),
#           " | ", str(round(text_code.count(alphabet[i]) / len(text_code), 4)).ljust(6),
#           " | ", str(round(text_code.count(dict[i]) / len(text_code), 4)).ljust(6), dict[i].ljust(3))

code_dict_bigram = {}
orig_dict_bigram = {}
# создание списка биграм
for i in range(0, len(alphabet)):
    for j in range(0, len(alphabet)):
        bigram.append((alphabet[i] + alphabet[j]))
for i in bigram:
    code_dict_bigram[i] = text_orig.count(i)
    orig_dict_bigram[i] = text_code.count(i)
    # print(i, str(text_orig.count(i)).ljust(5),
    #       " | ", str(text_code.count(i)).ljust(5))
code_dict_bigram = sorted(code_dict_bigram.items(), key=operator.itemgetter(1))
print(code_dict_bigram)
orig_dict_bigram = sorted(orig_dict_bigram.items(), key=operator.itemgetter(1))
print(orig_dict_bigram)

print("кодированный"," | ","оригинальный")
for i in range(len(code_dict_bigram)-1,len(code_dict_bigram)-6,-1):
    print(orig_dict_bigram[i][1]/len(text_orig), code_dict_bigram[i][1]/len(text_orig))

fclear = open("outp_clear.txt", "w+", encoding="utf-8")
fclear.write(text_orig)
fcode = open("outp_code.txt", "w+", encoding="utf-8")
fcode.write(text_code)

dictDecode = [i for i in range(0,33 )]
for i in range(0,len(code_dict_bigram)):
    for j in range(0,len(code_dict_bigram)):
        if orig_dict_bigram[i][1]/len(text_orig) == code_dict_bigram[i][1]/len(text_orig) and orig_dict_bigram[j][1]/len(text_orig) > 0:
            # print(alphabet.find(orig_dict_bigram[i][0][0]))
            dictDecode[alphabet.find(code_dict_bigram[i][0][0])] = orig_dict_bigram[i][0][0]
            dictDecode[alphabet.find(code_dict_bigram[i][0][1])] = orig_dict_bigram[i][0][1]

            # print(orig_dict_bigram[i][1]/len(text_orig), code_dict_bigram[i][1]/len(text_orig))
            # dictDecode.replace(orig_dict_bigram[i][0][0],code_dict_bigram[i][0][0])
            # print(orig_dict_bigram[i][0][0],code_dict_bigram[i][0][0])
            # dictDecode.replace(orig_dict_bigram[i][0][1],code_dict_bigram[i][0][1])

print(dictDecode)

text_decode = ""
# for i in range(0,len(dictDecode)):
#     print(dictDecode[i], "=>", alphabet[i])
# text_code += dict[alphabet.find(char)]
for char in text_code:
    if char == " ":
        text_decode += " "
    else:
        text_decode += alphabet["".join(dictDecode).find(char)]
        # print("".join(dictDecode).find(char), alphabet["".join(dictDecode).find(char)])

print(text_decode)

decoded = open("decoded.txt", "w+", encoding="utf-8")
decoded.write(text_decode)



print("--- %s seconds ---" % (time.time() - start_time))