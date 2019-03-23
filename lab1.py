import re

shift = "дюмях"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" #[chr(i) for i in range(1072, 1072+32)]
bigram = []
dict = alphabet
reg_ex = re.compile('[^а-яА-Я ]')

print(list(alphabet))

for chr in list(shift):
    dict = dict.replace(chr, '')

for i in range(0, len(alphabet)):
    for j in range(0, len(alphabet)):
        bigram.append((alphabet[i]+alphabet[j]))
# создание словаря с заданным правилом
dict = shift + dict
print(list(dict), len(alphabet), len(dict))

file = open("v   i mir.txt", "r",encoding="utf-8")
text = file.read()

# удаление некириллических символов
text_orig = reg_ex.sub('', text).lower()
text_code = ""
'''
for i,char in enumerate(dict):
    text_code = text_code.replace(alphabet[i],char)
'''
for char in text_orig:
    if char == " ":
        text_code += " "
    else:
        text_code += dict[alphabet.find(char)]
for i in range(0,len(dict)):
    # print(alphabet[i].ljust(3)," | ", str(text_orig.count(alphabet[i])).ljust(6), " | ", str(text_code.count(alphabet[i])).ljust(6),
    #       dict[i].ljust(3), " | ", str(text_orig.count(dict[i])).ljust(6), " | ", str(text_code.count(dict[i])).ljust(6))
    print(alphabet[i].ljust(3), " | ",
          str(text_orig.count(alphabet[i])).ljust(6),
          " | ", str(text_code.count(alphabet[i])).ljust(6),
          " | ", str(text_code.count(dict[i])).ljust(6),
          dict[i].ljust(3))
# вывод процентных значений
print()
for i in range(0,len(dict)):
    print(alphabet[i].ljust(3),
          " | ", str(round(text_orig.count(alphabet[i])/len(text_orig),4)).ljust(6),
          " | ", str(round(text_code.count(alphabet[i])/len(text_code),4)).ljust(6),
          " | ", str(round(text_code.count(dict[i])/len(text_code),4)).ljust(6),dict[i].ljust(3))

# print(text_orig)
# print(text_code)
for i in bigram:
    print(i, text_orig.count(i))
fclear= open("outp_clear.txt","w+")
fclear.write(text_orig)
fcode= open("outp_code.txt","w+")
fcode.write(text_code)